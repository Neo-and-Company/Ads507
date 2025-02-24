variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "db_name" {
  type    = string
  default = "AdventureSales"
}

variable "db_user" {
  type    = string
  default = "Ads507"
}

variable "db_pass" {
  type    = string
  default = "Gabrielleo24"
  sensitive = true
}

variable "vpc_id" {
  type    = string
  default = "vpc-0f7781a0ffdd06b70"  # or your actual VPC ID
}

variable "my_ip" {
  type    = string
  default = "0.0.0.0/0"  # Not recommended for production
}