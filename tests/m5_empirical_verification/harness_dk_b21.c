#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "/mnt/second_drive/DOCS/SEC/tests/m5_empirical_verification/snippets/dk_b21_L1250_c.c"

static char mock_device_buffer[256] = "Hello POSIX VFS!";

static ssize_t mock_read(struct vfs_file *file, char *buf, size_t count, loff_t *pos) {
    (void)file;
    size_t len = strlen(mock_device_buffer);
    if (*pos >= (loff_t)len) return 0;
    if (count > len - *pos) count = len - *pos;
    memcpy(buf, mock_device_buffer + *pos, count);
    *pos += count;
    return count;
}

static ssize_t mock_write(struct vfs_file *file, const char *buf, size_t count, loff_t *pos) {
    (void)file;
    if (*pos + count >= sizeof(mock_device_buffer)) {
        count = sizeof(mock_device_buffer) - 1 - *pos;
    }
    memcpy(mock_device_buffer + *pos, buf, count);
    mock_device_buffer[*pos + count] = '\0';
    *pos += count;
    return count;
}

static loff_t mock_llseek(struct vfs_file *file, loff_t offset, int whence) {
    if (whence == 0) file->f_pos = offset;
    return file->f_pos;
}

static const struct file_operations mock_fops = {
    .read = mock_read,
    .write = mock_write,
    .open = NULL,
    .release = NULL,
    .llseek = mock_llseek,
    .fsync = NULL
};

int main(void) {
    printf("Testing dk_b21: Linux VFS File Operations & File Struct...\n");

    struct vfs_file file;
    file.f_dentry = NULL;
    file.f_op = &mock_fops;
    file.f_flags = 0;
    file.f_pos = 0;
    file.private_data = NULL;

    char read_buf[64] = {0};
    ssize_t bytes_read = file.f_op->read(&file, read_buf, sizeof(read_buf), &file.f_pos);
    assert(bytes_read == 16);
    assert(strcmp(read_buf, "Hello POSIX VFS!") == 0);
    assert(file.f_pos == 16);

    /* Test write */
    file.f_op->llseek(&file, 0, 0);
    assert(file.f_pos == 0);
    const char *new_data = "Kernel VFS Verified!";
    ssize_t bytes_written = file.f_op->write(&file, new_data, strlen(new_data), &file.f_pos);
    assert(bytes_written == (ssize_t)strlen(new_data));
    assert(strcmp(mock_device_buffer, "Kernel VFS Verified!") == 0);

    printf("dk_b21 verified successfully: VFS file_operations dispatch functioning perfectly!\n");
    return 0;
}
