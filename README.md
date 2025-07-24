# AWS

### 311 - EC2, S3
* EC2 인스턴스 조회 - Instance ID, Instance Type, Private IP Address, LaunchTime
* S3 Bucket 조회 - Name, Creation Time
<p>region을 입력받으면 조회.</p>


### 312 - VPC
* VPC 생성 <br>
입력(region, CIDR)을 통해 VPC 생성.
* 서브넷 생성 <br>
private/public 서브넷 생성을 위한 입력(개수, CIDR, 개수)을 받고 생성.
* Internet Gateway 생성 <br>
public 서브넷에 연결할 Internet Gateway생성.
* pulic 서브넷에 연결할 Routing Table 생성 <br>
Routing Table 생성 후 Internet Gateway 연결. public 서브넷과 연결.
* NAT Gateway 생성 <br>
EIP 할당 후 private 서브넷에 연결한 NAT Gateway 생성.
* private 서브넷에 연결한 Routing Table 생성 <br>
Routing Table 생성 후 NAT Gateway 연결. private 서브넷과 연결.
* Security Group 생성 <br>
모든 outbound가 허용인 Security Group 생성.
