# Chương 8 – Mạng không dây & IoT (Wireless & IoT)

## 1. Mục tiêu
- Hiểu các chuẩn **Wi‑Fi (802.11 a/b/g/n/ac/ax)**, **Bluetooth Low Energy (BLE)**, **Zigbee**, **LoRaWAN**.
- Nắm cách cấu hình **Wi‑Fi** trên Linux (NetworkManager, `iw`), **BLE** scanning, và **IoT gateway**.
- Thực hành nhanh: quét mạng Wi‑Fi, kết nối tới Access Point, đọc dữ liệu BLE.

## 2. Các chuẩn không dây quan trọng
| Chuẩn | Băng tần | Tốc độ tối đa | Ứng dụng |
|-------|----------|----------------|----------|
| **802.11a** | 5 GHz | 54 Mbps | môi trường ít nhiễu.
| **802.11b** | 2.4 GHz | 11 Mbps | thiết bị cũ.
| **802.11g** | 2.4 GHz | 54 Mbps | phổ thông.
| **802.11n** | 2.4/5 GHz | 600 Mbps | MIMO.
| **802.11ac** | 5 GHz | up to 3.5 Gbps | streaming 4K.
| **802.11ax (Wi‑Fi 6)** | 2.4/5 GHz | up to 9.6 Gbps | môi trường đông người.
| **BLE** | 2.4 GHz | ~1 Mbps | thiết bị low‑power.
| **Zigbee** | 2.4 GHz | 250 kbps | nhà thông minh.
| **LoRaWAN** | sub‑GHz | 0.3‑50 kbps | IoT rộng vùng.

## 3. Thực hành nhanh (CLI)
### a. Quét Wi‑Fi với `iw`
```bash
# Kiểm tra interface không dây
iw dev

# Quét các mạng khả dụng
sudo iw dev wlan0 scan | grep SSID
```
### b. Kết nối tới một AP (NetworkManager)
```bash
nmcli dev wifi list               # hiển thị danh sách SSID
nmcli dev wifi connect "MySSID" password "mypassword"
```
### c. Kiểm tra tín hiệu RSSI
```bash
iwconfig wlan0 | grep -i signal
```
### d. Scan BLE thiết bị với `bluetoothctl`
```bash
bluetoothctl
[bluetooth]# scan on
# Đợi vài giây, sau đó lệnh `devices` sẽ liệt kê MAC và tên.
```
### e. Khởi chạy một **IoT gateway** nhẹ (Node‑RED) trên Docker
```bash
docker run -d -p 1880:1880 --name nodered nodered/node-red
```

## 4. Mini‑quiz
1. Wi‑Fi 802.11ax cải thiện điều gì so với 802.11ac? 
2. BLE hoạt động ở băng tần nào? 
3. Lệnh `nmcli dev wifi connect` thực hiện gì? 
4. Độ trễ (latency) thường thấp hơn trong giao thức nào: BLE hay Zigbee? 
5. Khi quét Wi‑Fi, chỉ số `RSSI` đo gì?

---
