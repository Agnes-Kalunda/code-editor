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
            elif language == 'javascript':
                result = run_javascript_code(code)
            else:
                result = "Language not supported for execution."

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})

# Functions for language-specific code execution
def run_python_code(code):
    try:
        result = subprocess.check_output(['python3', '-c', code], text=True, timeout=5)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def run_php_code(code):
    # Execute PHP code using a dedicated library or method
    # You might need to install a library like phpserialize
    import phpserialize
    result = phpserialize.phpserialize(code)  # Replace with your actual PHP execution logic
    return result

def run_javascript_code(code):
    # Execute JavaScript code using a JavaScript engine
    import execjs  # Requires execjs library
    context = execjs.compile(code)
    result = context.call('eval', code)
    return result