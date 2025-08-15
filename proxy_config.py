import requests

def make_proxied_request(url, proxy_address):
    proxies = {
        "http": proxy_address,
        "https": proxy_address,
    }
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        print(f"Requisição bem-sucedida para {url} via {proxy_address}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição via proxy {proxy_address}: {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso (substitua por um proxy real e um URL de teste)
    test_url = "http://httpbin.org/ip"
    # Você precisaria de um serviço de proxy para obter um endereço real
    # Ex: "http://user:password@proxy.example.com:8080"
    # Ou um proxy gratuito para testes (não recomendado para uso em produção)
    proxy_example = "http://127.0.0.1:8080" # Substitua pelo seu proxy

    print(f"Tentando requisição para {test_url} via proxy {proxy_example}")
    content = make_proxied_request(test_url, proxy_example)
    if content:
        print("Conteúdo recebido:")
        print(content)


