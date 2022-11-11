# Đề tài 14 :Xây dựng ứng dụng trên AWS cho phép tạo Database và cung cấp API để thêm,xóa sửa trên Database 

## Các tính năng chính

- Đăng ký tài khoản để sử dụng các dịch vụ của Website
- Thêm, xóa, sửa Database của MySQL
- Thêm, xóa, sửa Table trong Database
- Thêm, xóa, sửa dữ liệu trong Table

## Công nghệ sử dụng

## Ngôn ngữ: Python 
## Client: HTML, CSS3, BOOTSTRAP 4, JavaScript
## Server: AWS Lambda, AWS SQS, AWS EC2,Flask Framework
## Database: MySQL

## Thành viên của nhóm

- 19133028 Đoàn Trần Đăng Khoa
- 19133038 Lê Thị Kim Ngân
- 19133055 Đào Thị Cẩm Tiên

## Chạy trên Localhost

Clone project từ github
```
  git clone https://github.com/ngan429/DETAI14.git
```

Truy cập thư mục chứa project

```bash
  cd DETAI14
```

Tạo môi trường ảo

```bash
  virtualenv venv
```

Kích hoạt môi trường ảo

```bash
  .\venv\Scripts\activate
```

Cài đặt các thư viện 

```bash
  pip install -r requirements.txt
```

Chạy file models

```bash
  python3
```

```bash
  from my_app import db
```

```bash
  from my_app.models import *
```

```bash
  db.create_all()
```

Chạy file run.py

```bash
  python3 run.py
```

Lưu ý: sẽ có một số máy khi clone về thiếu thư viện cần thiết, nạp các thư viện theo yêu cầu


## Deploy lên AWS EC2 

```
Khởi động CMD , get SSH
```

Cài đặt và update

```bash
  sudo apt-get update
```

```bash
sudo apt-get install python3
```

```bash
sudo apt-get install python3-pip
```
Nếu muốn kiểm tra lại dùng lệnh

```bash
whereis python
```

```bash
whereis pip3
```

Cài đặt các thư viện cần thiết
```bash
sudo pip3 install flask
```

```bash
sudo apt-get install nginx
```

```bash
sudo apt-get install gunicorn3
```

Dùng git clone để project về 

```bash
  git clone https://github.com/ngan429/DETAI14.git
```

Truy cập vào flaskapplication
```bash
mkdir flaskapplication
```

```bash
mkdir flaskapplication
```

```bash
cd DETAI14
```

```bash
cd Detai14_Project
```

Truy cập file run.py

```bash
  vi run.py
```

Thay đổi file run.py từ 

```python3
  from my_app import app
  app.run(debug=True)
```

Sang cấu hình phù hợp với máy ảo EC2

```python3
  from my_app import app
  app.run(host='0.0.0.0', port=8080)
```

```bash
  python3 run.py
```
Có thể sẽ thiếu thư viện cần thiết, có thể cài theo thư viện yêu cầu để chạy được 

