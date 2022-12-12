# Đề tài 14 :Xây dựng ứng dụng trên AWS cho phép tạo Database và cung cấp API để thêm,xóa sửa trên Database 

## Các tính năng chính

- Đăng ký tài khoản để sử dụng các dịch vụ của Website
- Thêm, xóa, sửa Database của MySQL
- Thêm, xóa, sửa Table trong Database
- Thêm, xóa, sửa dữ liệu trong Table

## Công nghệ sử dụng
## Ngôn ngữ: Python 
## Thư Viện: boto3,,Flask Framework,...
## Server: AWS Lambda, AWS SQS, AWS EC2
## Database: MySQL

## Thành viên của nhóm

- 20110502 Phan Duy Khánh
- 20110088 Nguyễn Anh Khoa
- 20110599 Hà Nhật Vềnh

## Chạy trên Localhost

Clone project từ github
```
  git clone https://github.com/DuyKhanh2002/Cloud_DeTai14.git
```

Truy cập thư mục chứa project

```bash
  cd Cloud_Nhom31
```

Cài đặt các thư viện 

```bash
  pip install -r requirements.txt
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

Cài đặt các thư viện cần thiết
```bash
sudo pip3 install flask
```
```bash
  pip install -r requirements.txt
```
```bash
sudo pip3 install boto3
```

Dùng git clone để project về 

```bash
  git clone https://github.com/DuyKhanh2002/Cloud_DeTai14.git
```

Truy cập vào project vừa git về:

```bash
cd Cloud_DeTai14
```

```bash
cd Cloud_Nhom31
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

