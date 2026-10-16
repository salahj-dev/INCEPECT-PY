
import requests as rq
import time 

url = (input("Enter the URL: "))
try:
    start = time.time()
    response = rq.get(url, timeout=5)
    end = time.time()
    elapsed_time = end - start
    print(f"Response time: {elapsed_time:.2f} seconds")
    print(f"Response headers: {response.headers}")
    print(f"Status code: {response.status_code}")
    print("=" * 69)
    print("=" * 69)
    
    
    
    # إذا كان رمز الحالة من 100 لـ 199 (معلومات)
    if 100 <= response.status_code <= 199:
        print(f"Informational: {response.status_code} - The request received an informational response.")
        print("=" * 69)



    # إذا كان رمز الحالة من 200 لـ 299 (نجاح)
    elif 200 <= response.status_code <= 299:
        print(f"Success: {response.status_code} - The request was successful.") 
        print("=" * 69)
        
        
        
    # إذا كان رمز الحالة من 300 لـ 399 (إعادة توجيه)
    elif 300 <= response.status_code <= 399:
        print(f"Redirection: {response.status_code} - Further action or redirection may be required.")
        print("=" * 69)
        
        
        
    # إذا كان رمز الحالة من 400 لـ 499 (خطأ من عند العميل/المستخدم)
    elif 400 <= response.status_code <= 499:
        print(f"Client Error: {response.status_code} - The request could not be fulfilled due to a client-side issue.")
        print("=" * 69)
        
        
        
        
# إذا كان رمز الحالة من 500 لـ 599 (خطأ في السيرفر)
    elif 500 <= response.status_code <= 599:
        print(f"Server Error: {response.status_code} - The server failed to fulfill the request.")
        print("=" * 69)
        
        
        
# إذا كان الرمز غير معروف
    else:
        print(f"Unknown Status: {response.status_code} - Unrecognized status code.")
        print("=" * 69)
    
    


except rq.exceptions.Timeout as e:
    print(f"The request timed out. The URL may be unreachable or taking too long to respond. Error details: {e}") 
    print("=" * 69)
    print("=" * 69)
    
    
except rq.exceptions.RequestException as e:
    print(f"An error occurred while fetching the URL Error details: {e}")
    print("=" * 69)
    print("=" * 69)
    
    
except Exception as e:
    print(f"An unexpected error occurred while fetching the URL: {e}")
    print("=" * 69)
    print("=" * 69)