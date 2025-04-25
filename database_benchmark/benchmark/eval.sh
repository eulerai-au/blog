#!/bin/bash

# 定义测试脚本路径和数据库服务配置
POSTGRESQL_SCRIPT="postgresql_benchmark.py"
MONGODB_SCRIPT="mongodb_benchmark.py"
SURREALDB_SCRIPT="surrealdb_benchmark.py"

MONGODB_SERVICE="mongod"
SURREALDB_BINARY="/home/shinshi/.surrealdb/surreal"

DATA_DIR="~/database_benchmark/graphy_raw_data"

# 检查操作是否成功的函数
check_success() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# 启动 PostgreSQL 服务
start_postgresql() {
    echo "Starting PostgreSQL service..."
    sudo systemctl start postgresql
    check_success "Failed to start PostgreSQL service"
    echo "PostgreSQL service started."
}

# 启动 MongoDB 服务
start_mongodb() {
    echo "Starting MongoDB service..."
    sudo systemctl start $MONGODB_SERVICE
    check_success "Failed to start MongoDB service"
    echo "MongoDB service started."
}

# 停止 MongoDB 服务
stop_mongodb() {
    echo "Stopping MongoDB service..."
    sudo systemctl stop $MONGODB_SERVICE
    check_success "Failed to stop MongoDB service"
    echo "MongoDB service stopped."
}

# 启动 SurrealDB 服务
start_surrealdb() {
    echo "Starting SurrealDB..."
    $SURREALDB_BINARY start --user root --pass 31415926 > surrealdb.log 2>&1 &
    SURREALDB_PID=$!
    sleep 5  # 等待 SurrealDB 启动完成
    if ! ps -p $SURREALDB_PID > /dev/null; then
        echo "Error: Failed to start SurrealDB"
        exit 1
    fi
    echo "SurrealDB started with PID $SURREALDB_PID."
}

# 停止 SurrealDB 服务
stop_surrealdb() {
    echo "Stopping SurrealDB..."
    kill $SURREALDB_PID
    check_success "Failed to stop SurrealDB"
    echo "SurrealDB stopped."
}

# 运行性能测试脚本
run_tests() {
    local script=$1
    echo "Running benchmark script: $script"
    python3 $script
    check_success "Benchmark script $script failed"
    echo "Benchmark script $script completed."
}

# 主函数：启动服务、运行测试、关闭服务
main() {
    echo "Starting database benchmark testing..."

    # 确保 PostgreSQL 服务常驻后台
    start_postgresql

    # 启动并测试 SurrealDB
    start_surrealdb
    run_tests $SURREALDB_SCRIPT
    stop_surrealdb

    # 启动并测试 MongoDB
    start_mongodb
    run_tests $MONGODB_SCRIPT
    stop_mongodb

    # 测试 PostgreSQL
    run_tests $POSTGRESQL_SCRIPT

    echo "Database benchmark testing completed!"
}

# 执行主函数
main