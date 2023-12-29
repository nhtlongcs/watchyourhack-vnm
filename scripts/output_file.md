---
title: Docker
lang-ref: Docker
---

[Docker](https://docs.docker.com) là một nền tảng dành cho những nhà phát triển và quản trị hệ thống để phát triển, vận chuyển và chạy ứng dụng. Docker cho phép bạn nhanh chóng tạo ứng dụng từ các thành phần và loại bỏ sự cản trở có thể xảy ra khi vận chuyển mã. Docker cho phép bạn kiểm tra và triển khai mã của bạn vào môi trường sản phẩm càng nhanh càng tốt. Với Docker, các nhà phát triển có thể xây dựng bất kỳ ứng dụng nào bằng bất kỳ ngôn ngữ nào sử dụng bất kỳ công cụ nào. Các ứng dụng "được Docker hóa" hoàn toàn có thể di chuyển và có thể chạy ở bất kỳ đâu - trên máy tính MacBook hoặc máy tính Windows của đồng nghiệp, các máy chủ kiểm tra chạy Ubuntu trên đám mây và máy ảo trung tâm dữ liệu sản xuất chạy Red Hat. ## Docker cho Mac

Docker cho Mac là phiên bản hiện tại của Docker cho macOS.

### Cài đặt

Bạn có thể tải về Docker cho Mac [tại đây] (https://docs.docker.com/docker-for-mac/install/).### Điều kiện tiên quyết

Bạn sẽ cần `homebrew-cask` để cài đặt Docker Toolbox, nếu bạn chưa có thì hãy tham khảo [phần này] (../Homebrew/Cask.md). Cài đặt

Có hai cách để cài đặt Docker

Tùy chọn 1: Đây là các bước để cài đặt docker bằng brew

- Cài đặt docker và docker machine từ brew

```sh
brew install docker docker-machine
```

- Cài đặt VirtualBox để Docker có thể tạo các hình ảnh. ```sh
  brew install --cask virtualbox

````

> Nếu bạn gặp vấn đề với trình cài đặt với thông báo lỗi như

```sh
Cài đặt không thành công (Trình cài đặt gặp lỗi dẫn đến việc cài đặt thất bại. Liên hệ nhà sản xuất phần mềm để được hỗ trợ.)```

> Sử dụng câu lệnh sau khi bạn gặp lỗi, bật Preferences hệ thống và kiểm tra xem 'Phần mềm Hệ thống từ nhà phát triển "Oracle America, inc" bị chặn khỏi tải. ' Nếu bạn thấy thông báo đó, hãy nhấp vào nút Cho phép và thử cài đặt lại.
Việc này sẽ hoàn tất việc cài đặt

---

Bây giờ để tạo một Machine, làm theo các bước sau:

```sh
docker-machine create --driver virtualbox default
````

Chạy lệnh sau đây để cho Docker biết máy nào thực thi Docker

```sh
docker-machine env default
```

Cuối cùng, để xác minh tất cả các bước cài đặt:

```sh
docker run hello-world
```

Bạn có thể tìm thêm thông tin về Docker trong [tài liệu](https://docs.docker.com/). Tùy chọn 2: Cài đặt bằng Docker App

- Truy cập vào đường dẫn sau:

```sh
https://hub.docker.com/editions/community/docker-ce-desktop-mac/
```

Việc cài đặt này sẽ cung cấp cho bạn tất cả các công cụ GUI cần thiết.
