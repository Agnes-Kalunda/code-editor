from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess

# Create your views here.
def home(request):
    return render(request, 'main.html')



@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code', '')
            language = request.POST.get('language', '')

            if language == 'python':
                result = run_python_code(code)
            elif language == 'php':
                result = run_php_code(code)
            elif language == 'c_cpp':
                result = run_c_cpp_code(code)
            else:
                result = "Language not supported for execution."

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})

def run_python_code(code):
    try:
        # Run Python code using Docker
        result = subprocess.check_output(['docker', 'run', '--rm', 'python:3.8', 'python', '-c', code], text=True)
        return result

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def run_php_code(code):
    try:
        # Run PHP code using Docker
        result = subprocess.check_output(['docker', 'run', '--rm', 'php:7.4-cli', 'php', '-r', code], text=True)
        return result

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def run_c_cpp_code(code):
    
    return "C++ code execution not implemented."