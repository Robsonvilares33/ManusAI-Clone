import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def human_like_mouse_move(driver, target_element, duration_min=0.2, duration_max=0.8):
    """
    Simula movimentos de mouse mais humanos para um elemento alvo, com duração variável.
    """
    try:
        actions = ActionChains(driver)
        # Move para o elemento com uma duração simulada
        actions.move_to_element(target_element).perform()
        time.sleep(random.uniform(duration_min, duration_max))
    except Exception as e:
        print(f"Erro ao simular movimento do mouse: {e}")

def human_like_type(element, text, delay_min=0.05, delay_max=0.2, error_rate=0.01):
    """
    Simula digitação humana com atrasos aleatórios e uma pequena taxa de erro/correção.
    """
    for char in text:
        if random.random() < error_rate: # Simula um erro de digitação
            element.send_keys(random.choice('abcdefghijklmnopqrstuvwxyz'))
            time.sleep(random.uniform(delay_min, delay_max))
            element.send_keys(Keys.BACK_SPACE) # Corrige o erro
            time.sleep(random.uniform(delay_min, delay_max))
        element.send_keys(char)
        time.sleep(random.uniform(delay_min, delay_max))

def human_like_scroll(driver, scroll_pixels=None, scroll_duration_min=0.5, scroll_duration_max=2.0):
    """
    Simula rolagem de página humana, com quantidade e duração variáveis.
    """
    if scroll_pixels is None:
        scroll_pixels = random.randint(200, 800) # Rolagem aleatória

    driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
    time.sleep(random.uniform(scroll_duration_min, scroll_duration_max))

def adaptive_wait(driver, by_locator, timeout=10, poll_frequency=0.5):
    """
    Espera adaptativamente por um elemento, simulando um tempo de reação humano.
    """
    try:
        wait_time = random.uniform(0.5, 2.0) # Simula tempo de reação
        time.sleep(wait_time)
        element = WebDriverWait(driver, timeout, poll_frequency=poll_frequency).until(
            EC.presence_of_element_located(by_locator)
        )
        return element
    except TimeoutException:
        print(f"Elemento não encontrado após {timeout} segundos: {by_locator}")
        return None
    except NoSuchElementException:
        print(f"Elemento não encontrado: {by_locator}")
        return None

def simulate_human_interaction_flow(driver, actions_list):
    """
    Simula um fluxo de interação humano mais complexo e adaptativo.
    actions_list: Lista de dicionários, onde cada dicionário define uma ação:
        {'type': 'click', 'element': target_element}
        {'type': 'type', 'element': input_element, 'text': 'some text'}
        {'type': 'scroll', 'pixels': 500}
        {'type': 'wait', 'locator': (By.ID, 'some_id')}
    """
    for action in actions_list:
        action_type = action.get('type')
        if action_type == 'click':
            element = action.get('element')
            if element:
                human_like_mouse_move(driver, element)
                element.click()
                time.sleep(random.uniform(1, 3))
        elif action_type == 'type':
            element = action.get('element')
            text = action.get('text')
            if element and text:
                human_like_mouse_move(driver, element)
                element.click() # Focar no campo de texto
                human_like_type(element, text)
                time.sleep(random.uniform(0.5, 1.5))
        elif action_type == 'scroll':
            pixels = action.get('pixels')
            human_like_scroll(driver, pixels)
        elif action_type == 'wait':
            locator = action.get('locator')
            if locator:
                adaptive_wait(driver, locator)
        # Adicionar mais tipos de ações conforme necessário (e.g., arrastar, soltar, passar mouse)

if __name__ == "__main__":
    print("Script de simulação de comportamento humano aprimorado para 'Soberania da Realidade'.")
    print("Inclui movimentos de mouse mais realistas, digitação com erros/correções, esperas adaptativas e fluxos de interação.")
    print("Para uso, integre as funções com seu driver Selenium/Appium e defina os fluxos de interação.")


