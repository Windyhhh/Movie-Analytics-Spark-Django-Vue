import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_genre_analysis(request):
    """获取按类型分析的数据"""
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                'data', 'processed', 'genre_analysis.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_year_analysis(request):
    """获取按年份分析的数据"""
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                'data', 'processed', 'year_analysis.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_rating_analysis(request):
    """获取评分分布分析的数据"""
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                'data', 'processed', 'rating_analysis.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_all_movies(request):
    """获取所有电影数据"""
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                'data', 'processed', 'movies.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def run_analysis(request):
    """运行Spark分析"""
    try:
        import subprocess
        import sys
        
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                 'data_processing', 'spark_analysis.py')
        
        # 运行Spark分析脚本
        result = subprocess.run([sys.executable, script_path], 
                               cwd=os.path.dirname(script_path),
                               capture_output=True, text=True)
        
        return JsonResponse({
            'success': True,
            'stdout': result.stdout,
            'stderr': result.stderr
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)