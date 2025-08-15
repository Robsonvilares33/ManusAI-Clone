import requests
import time
import base64

def solve_image_captcha(api_key, image_path):
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    payload = {
        'key': api_key,
        'method': 'base64',
        'body': image_base64
    }
    try:
        response = requests.post("http://2captcha.com/in.php", data=payload)
        response.raise_for_status()
        if "OK" in response.text:
            captcha_id = response.text.split("|")[1]
            print(f"CAPTCHA de imagem enviado, ID: {captcha_id}. Aguardando resolução...")
            while True:
                result_response = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}")
                result_response.raise_for_status()
                if "OK" in result_response.text:
                    return result_response.text.split("|")[1]
                elif "CAPCHA_NOT_READY" in result_response.text:
                    time.sleep(5)
                else:
                    raise Exception(f"Erro ao resolver CAPTCHA: {result_response.text}")
        else:
            raise Exception(f"Erro ao enviar CAPTCHA: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição ao serviço de CAPTCHA: {e}")
        return None

def solve_recaptcha_v2(api_key, site_key, page_url):
    payload = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': page_url
    }
    try:
        response = requests.post("http://2captcha.com/in.php", data=payload)
        response.raise_for_status()
        if "OK" in response.text:
            captcha_id = response.text.split("|")[1]
            print(f"reCAPTCHA v2 enviado, ID: {captcha_id}. Aguardando resolução...")
            while True:
                result_response = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}")
                result_response.raise_for_status()
                if "OK" in result_response.text:
                    return result_response.text.split("|")[1]
                elif "CAPCHA_NOT_READY" in result_response.text:
                    time.sleep(5)
                else:
                    raise Exception(f"Erro ao resolver reCAPTCHA v2: {result_response.text}")
        else:
            raise Exception(f"Erro ao enviar reCAPTCHA v2: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição ao serviço de CAPTCHA: {e}")
        return None

if __name__ == "__main__":
    # Substitua 'YOUR_2CAPTCHA_API_KEY' pela sua chave de API real
    # É altamente recomendável usar variáveis de ambiente para chaves de API
    api_key = "YOUR_2CAPTCHA_API_KEY"

    # Exemplo de uso para CAPTCHA de imagem (você precisaria de um arquivo de imagem de CAPTCHA)
    # try:
    #     resolved_text = solve_image_captcha(api_key, "path/to/your/captcha_image.png")
    #     if resolved_text:
    #         print(f"CAPTCHA de imagem resolvido: {resolved_text}")
    # except Exception as e:
    #     print(f"Falha ao resolver CAPTCHA de imagem: {e}")

    # Exemplo de uso para reCAPTCHA v2 (substitua com site_key e page_url reais)
    # site_key = "YOUR_RECAPTCHA_SITE_KEY"
    # page_url = "https://www.example.com/"
    # try:
    #     resolved_token = solve_recaptcha_v2(api_key, site_key, page_url)
    #     if resolved_token:
    #         print(f"reCAPTCHA v2 resolvido: {resolved_token}")
    # except Exception as e:
    #     print(f"Falha ao resolver reCAPTCHA v2: {e}")

    print("Script de contorno de CAPTCHA pronto para integração. Lembre-se de usar com responsabilidade e eticamente.")


