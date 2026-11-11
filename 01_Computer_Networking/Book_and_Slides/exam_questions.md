# Exam Questions: Mạng Máy Tính

## Multiple‑Choice (5 questions)

1. **Which layer of the TCP/IP model is responsible for routing packets across different networks?**
   - A) Application
   - B) Transport
   - C) Internet **(Correct)**
   - D) Link
   > *Explanation:* The Internet layer (IP) handles logical addressing and routing.

2. **What is the maximum size of the TCP header without options?**
   - A) 20 bytes **(Correct)**
   - B) 24 bytes
   - C) 32 bytes
   - D) 40 bytes
   > *Explanation:* Fixed TCP header is 20 bytes; options can extend up to 60 bytes.

3. **Which protocol uses port 53 and can operate over both TCP and UDP?**
   - A) HTTP
   - B) DNS **(Correct)**
   - C) SMTP
   - D) DHCP
   > *Explanation:* DNS primarily uses UDP for queries, TCP for zone transfers.

4. **In Ethernet CSMA/CD, after a collision is detected, the back‑off time is chosen from:**
   - A) A fixed 1 ms delay
   - B) A random value between 0 and 2ⁿ‑1 slot times, where *n* is the retry count **(Correct)**
   - C) The round‑trip time (RTT)
   - D) The TTL value of the frame
   > *Explanation:* Binary exponential back‑off selects a random slot count.

5. **Which of the following statements about the TCP sliding‑window mechanism is FALSE?**
   - A) The receiver advertises the window size to the sender.
   - B) The window size limits the amount of unacknowledged data.
   - C) The window size is measured in packets, not bytes.
   - D) A larger window can increase throughput on high‑delay links.
   - **Answer:** C **(Correct)**
   > *Explanation:* Window size is advertised in bytes.

---

## Short‑Answer / Essay (3 questions)

1. **Explain the end‑to‑end delay formula $D_{total}=D_{proc}+D_{queue}+D_{trans}+D_{prop}$, describing each component and how it impacts performance on a congested network.**
   *Your answer should reference processing at routers, queuing due to load, transmission time based on packet size and link rate, and propagation delay based on distance and medium speed.*

2. **Describe the three‑step TCP handshake, including the purpose of each flag (SYN, ACK) and how sequence numbers are used to establish a reliable connection.**
   *Include a diagram of the handshake and discuss how the initial sequence numbers protect against old duplicate segments.*

3. **Discuss the differences between IPv4 subnetting using classful boundaries and CIDR notation. Provide an example converting a class C network `192.168.1.0/24` into four equal subnets, showing the new prefix length, subnet masks, and usable host ranges.**
   *Explain why CIDR is more flexible and how it reduces waste of IP addresses.*
