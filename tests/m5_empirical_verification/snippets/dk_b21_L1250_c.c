#include <sys/types.h>
#include <stdint.h>

typedef int64_t loff_t;

struct vfs_file;
struct vfs_inode;
struct vfs_dentry;

/* Function pointer table for file operations */
struct file_operations {
    ssize_t (*read)(struct vfs_file *file, char *buf, size_t count, loff_t *pos);
    ssize_t (*write)(struct vfs_file *file, const char *buf, size_t count, loff_t *pos);
    int (*open)(struct vfs_inode *inode, struct vfs_file *file);
    int (*release)(struct vfs_inode *inode, struct vfs_file *file);
    loff_t (*llseek)(struct vfs_file *file, loff_t offset, int whence);
    int (*fsync)(struct vfs_file *file, loff_t start, loff_t end, int datasync);
};

/* VFS File object created on open() */
struct vfs_file {
    struct vfs_dentry              *f_dentry;   /* Associated directory entry */
    const struct file_operations   *f_op;       /* Dispatch table */
    uint32_t                        f_flags;    /* O_RDONLY, O_WRONLY, O_SYNC */
    loff_t                          f_pos;      /* Current file read/write offset */
    void                           *private_data;
};
