from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum
import json
import os

def main():
    # 创建Spark会话
    spark = SparkSession.builder \
        .appName("Movie Analytics") \
        .master("local[*]") \
        .getOrCreate()
    
    # 读取数据
    data_path = "../data/movies.csv"
    df = spark.read.csv(data_path, header=True, inferSchema=True)
    
    print("原始数据预览:")
    df.show(5)
    
    # 1. 按类型统计电影数量和平均评分
    genre_analysis = df.groupBy("genre") \
        .agg(count("movie_id").alias("movie_count"), \
             avg("rating").alias("avg_rating"), \
             sum("votes").alias("total_votes")) \
        .orderBy(col("movie_count").desc())
    
    print("\n按类型分析结果:")
    genre_analysis.show()
    
    # 2. 按年份统计电影数量
    year_analysis = df.groupBy("release_year") \
        .agg(count("movie_id").alias("movie_count")) \
        .orderBy("release_year")
    
    print("\n按年份分析结果:")
    year_analysis.show()
    
    # 3. 评分分布统计
    rating_analysis = df.groupBy("rating") \
        .agg(count("movie_id").alias("movie_count")) \
        .orderBy(col("rating").desc())
    
    print("\n评分分布分析:")
    rating_analysis.show()
    
    # 将分析结果转换为JSON格式，供前端使用
    output_dir = "../data/processed"
    os.makedirs(output_dir, exist_ok=True)
    
    # 转换为Pandas DataFrame以便处理
    genre_df = genre_analysis.toPandas()
    year_df = year_analysis.toPandas()
    rating_df = rating_analysis.toPandas()
    
    # 保存为JSON
    genre_df.to_json(os.path.join(output_dir, "genre_analysis.json"), orient="records")
    year_df.to_json(os.path.join(output_dir, "year_analysis.json"), orient="records")
    rating_df.to_json(os.path.join(output_dir, "rating_analysis.json"), orient="records")
    
    # 保存完整电影数据
    df.toPandas().to_json(os.path.join(output_dir, "movies.json"), orient="records")
    
    print(f"\n分析结果已保存到 {output_dir} 目录")
    
    # 停止Spark会话
    spark.stop()

if __name__ == "__main__":
    main()