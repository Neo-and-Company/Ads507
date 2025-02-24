output "db_endpoint" {
  description = "The endpoint of the MySQL RDS"
  value       = aws_db_instance.mysql_rds.endpoint
}