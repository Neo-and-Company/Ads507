provider "aws" {
  region = "us-east-1"
}

# Security Group to allow inbound MySQL traffic on port 3306
resource "aws_security_group" "allow_mysql" {
  name        = "allow_mysql_inbound"
  description = "Allow inbound traffic for MySQL"
  vpc_id      = var.vpc_id  # Ensure you have a variable or hard-code your VPC ID

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Adjust this to restrict access if needed
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# MySQL RDS Instance
resource "aws_db_instance" "my_rds" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  name                 = "AdventurePurchasing"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true

  vpc_security_group_ids = [aws_security_group.allow_mysql.id]
}
