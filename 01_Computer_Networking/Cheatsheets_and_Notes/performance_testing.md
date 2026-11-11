# Chương 9 – Kiểm tra & đo lường hiệu năng mạng (Performance Testing)

## 1. Mục tiêu
- Nắm các **công cụ đo băng thông** và độ trễ: `ping`, `iperf3`, `netperf`, `ttcp`.
- Hiểu **QoS**, **traffic shaping**, **latency vs jitter**.
- Thực hành đo tốc độ link, phân tích kết quả, tạo báo cáo nhanh.

## 2. Các chỉ số quan trọng
| Chỉ số | Ý nghĩa |
|--------|----------|
| **Throughput** (Mbps) | Lượng dữ liệu truyền qua trong một khoảng thời gian.
| **Latency** (ms) | Thời gian truyền một gói từ nguồn đến đích.
| **Jitter** (ms) | Độ biến thiên của latency (đặc biệt quan trọng cho VoIP, video).
| **Packet loss** (%) | Tỷ lệ gói mất mát, ảnh hưởng tới chất lượng.
| **QoS** | Đánh ưu tiên lưu lượng, giảm jitter, đảm bảo bandwidth cho ứng dụng quan trọng.

## 3. Công cụ đo lường phổ biến
- **ping** – đo latency, loss.
- **iperf3** – đo throughput TCP/UDP, hỗ trợ đa luồng.
- **netperf** – đo latency, cả TCP và UDP.
- **ttcp** – đo throughput đơn giản.
- **nload**, **bmon**, **ifstat** – giám sát traffic thời gian thực.
- **Wireshark** – phân tích chi tiết gói tin.

## 4. Thực hành nhanh (CLI)
### a. Đo latency và packet loss với `ping`
```bash
ping -c 10 8.8.8.8
```
Kết quả sẽ bao gồm **min/avg/max/stddev** và % loss.

### b. Đo throughput TCP với `iperf3`
```bash
# Trên server (có IP 192.168.1.10)
iperf3 -s

# Trên client
iperf3 -c 192.168.1.10 -t 30 -P 4   # 4 luồng, chạy 30s
```
Kết quả cho **Mbps** và **retrains**.

### c. Đo throughput UDP (thử độ trễ, jitter)
```bash
iperf3 -c 192.168.1.10 -u -b 50M -t 20
```
### d. Kiểm tra QoS với `tc`
```bash
# Thêm shaping 10Mbps cho eth0
sudo tc qdisc add dev eth0 root tbf rate 10mbit burst 32kbit latency 400ms

# Xóa shaping
sudo tc qdisc del dev eth0 root
```
### e. Giám sát traffic thời gian thực
```bash
nload -m
bmon -p eth0 -r
```

## 5. Mini‑quiz
1. Lệnh `iperf3 -c <server> -u -b 100M` đo gì? 
2. Trong `tc`, tham số `rate` xác định gì? 
3. Jitter ảnh hưởng lớn nhất tới loại ứng dụng nào? 
4. Khi `ping` báo loss 0%, nhưng `iperf3` cho throughput thấp, nguyên nhân có thể là gì? 
5. Để ưu tiên lưu lượng video, bạn sẽ dùng cơ chế gì trong Linux? (ví dụ: `tc`, `iptables` MARK, `tc class`)

---
