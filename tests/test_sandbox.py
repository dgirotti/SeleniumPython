import pytest
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("El botón muestra un Label a los 3 segundos de hacer click.")
@allure.epic("Interfaz Web")
@allure.feature("Botón con ID Dinámico")
@allure.story(
    "El texto aparece a los 3 segundos de hacer click en el botón con ID Dinámico"
)
@allure.testcase("IS-137")
@pytest.mark.sandbox
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    with allure.step("Al navegar al sandbox y hacer click en el botón con ID Dinámico"):
        sandbox_page.navigate_sandbox()
        sandbox_page.click_boton_id_dinamico()

    with allure.step("Y esperar los 3 segundos de delay que tiene el texto a aparecer"):
        elemento_texto_oculto = sandbox_page.wait_for_element(
            sandbox_page.HIDDEN_TEXT_LABEL
        )
    with allure.step("Puedo verificar que efectivamente el botón muestra un texto"):

        texto_esperado = (
            "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
        )

        assert (
            texto_esperado in elemento_texto_oculto.text
        ), "El texto esperado no coincide con el texto encontrado"


@allure.title("El botón con ID dinámico cambia de color al hacer hover over.")
@allure.epic("Interfaz Web")
@allure.feature("Botón con ID Dinámico")
@allure.story("El componente botón debería cambiar de color al posar el mouse sobre él")
@allure.testcase("IS-138")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.sandbox
def test_boton_id_dinamico_cambiar_color_al_hacer_hover(sandbox_page):
    with allure.step(
        "Al navegar al sandbox verificar que el botón es de un color dado"
    ):
        sandbox_page.navigate_sandbox()
        boton_id_dinamico = sandbox_page.wait_for_element(
            sandbox_page.DYNAMIC_ID_BUTTON
        )
        color_before_hover = boton_id_dinamico.value_of_css_property("background-color")
    with allure.step(
        "Cuando hago hover sobre el control del botón con ID Dinámico y ver su color"
    ):
        sandbox_page.hover_over_dynamic_id_button()
        color_after_hover = boton_id_dinamico.value_of_css_property("background-color")
    with allure.step(
        "Puedo verificar que el color que tenía antes y después del hover over, son distintos"
    ):
        assert color_before_hover != color_after_hover


@allure.title(
    "Podemos elegir el checkbox asociado a un alimento en el componente checkboxes comida"
)
@allure.epic("Interfaz Web")
@allure.feature("Checkboxes comida")
@allure.story("El usuario puede elegir un valor del checkbox con comidas")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("IS-139")
@pytest.mark.sandbox
def test_elegir_checkbox(sandbox_page):
    label_text = "Pizza"
    with allure.step("Dado que navego al sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step(
        "Puedo elegir un alimento clickeando en el checkbox asociado a él."
    ):
        sandbox_page.select_checkbox_with_label(label_text)
        assert sandbox_page.is_checkbox_selected(
            label_text
        ), f"El checkbox para {label_text} no está seleccionado después de hacerle click."


@allure.title("Puedo seleccionar un radio button.")
@allure.epic("Interfaz Web")
@allure.feature("Radio Buttons")
@allure.story("El usuario puede seleccionar un radio button")
@allure.testcase("IS-140")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sandbox
def test_elegir_radio_button(sandbox_page):
    opcion_radio_button = "No"
    with allure.step(
        f"Dado que navego al sandbox y selecciono el radio button que dice {opcion_radio_button}"
    ):
        sandbox_page.navigate_sandbox()
        sandbox_page.select_radio_button(opcion_radio_button)
    with allure.step(
        f"Puedo validar que el botón {opcion_radio_button} ha sido seleccionado correctamente."
    ):
        assert sandbox_page.is_radio_button_selected(
            opcion_radio_button
        ), f"El radio button '{opcion_radio_button}' no está seleccionado."


@allure.title("Puedo seleccionar un deporte del dropdown Deportes.")
@allure.epic("Interfaz Web")
@allure.feature("Dropdown Deportes")
@allure.story("El usuario puede seleccionar un deporte.")
@allure.testcase("IS-141")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sandbox
def test_elegir_deporte_del_dropdown(sandbox_page):
    deporte = "Fútbol"
    with allure.step("Dado que navego al sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step(f"Puedo seleccionar {deporte} en el dropdown Deportes"):
        sandbox_page.select_deporte(deporte)


@allure.title("La lista de Deportes en el dropdown deportes es la esperada.")
@allure.epic("Interfaz Web")
@allure.feature("Dropdown Deportes")
@allure.story("Lista de deportes")
@allure.testcase("IS-142")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.sandbox
def test_deporte_dropdown_options(sandbox_page):
    with allure.step("Dado que navego al sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("Y obtengo la lista de deportes en el dropdown."):
        options = sandbox_page.get_deporte_dropdown_options()
    with allure.step(
        "Puedo validar que la lista presente es acorde con los requerimientos."
    ):
        expected_options = ["Seleccioná un deporte", "Fútbol", "Tennis", "Basketball"]

        assert all(
            option in options for option in expected_options
        ), "No todas las opciones esperadas están presentes en el select"


@allure.title(
    "El texto 'Popup de ejemplo' aparece dentro de un popup al clickear el botón 'Popup'"
)
@allure.epic("Interfaz Web")
@allure.feature("Popup")
@allure.story("El usuario ve un popup al clickear en el botón Popup")
@allure.testcase("IS-143")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sandbox
def test_popup_title(sandbox_page):
    with allure.step("Dado que navego al Sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("Y hago click en el botón Popup"):
        sandbox_page.click_boton_popup()
    with allure.step(
        "Puedo validar que el texto 'Popup de ejemplo' aparece dentro de un popup."
    ):
        popup_title_text = sandbox_page.get_popup_title_text()
        expected_text = "Popup de ejemplo"

        assert (
            popup_title_text == expected_text
        ), f"El texto del popup es incorrecto, se obtuvo '{popup_title_text}' en su lugar."


@allure.title(
    "La tabla dinámica cambia el valor de la celda al hacer un reload de la página."
)
@allure.epic("Interfaz Web")
@allure.feature("Tabla dinámica")
@allure.story(
    "La tabla dinámica cambia los valores de sus celdas al hacer un reload a la página."
)
@allure.testcase("IS-144")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sandbox
def test_valor_celda_cambia_post_recarga(sandbox_page):
    with allure.step("Dado que navego a la página sandbox."):
        sandbox_page.navigate_sandbox()
    with allure.step("Y tomo el valor de una celda como ejemplo."):
        valor_inicial = sandbox_page.get_celda_valor(2, 3)
    with allure.step("Al hacer un reload a la página web."):
        sandbox_page.reload_page()
    with allure.step("Puedo ver que el valor para la celda es distinto."):
        valor_post_recarga = sandbox_page.get_celda_valor(2, 3)

        assert (
            valor_inicial != valor_post_recarga
        ), f"El valor de la celda no cambió después de la recarga; aún es '{valor_inicial}'."


@allure.title(
    "El valor de las celdas NO cambia cuando hay una recarga de la página para la tabla estática"
)
@allure.epic("Interfaz Web")
@allure.feature("Tabla estática")
@allure.story("Comportamiento Celdas")
@allure.testcase("IS-145")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://github.com/TheFreeRangeTester/sandbox-automation-testing/issues/5"
)
@pytest.mark.sandbox
def test_valor_celda_no_cambia_post_recarga(sandbox_page):
    with allure.step(
        "Dado que navego al sandbox de Free Range Testers y tomo como referencia una celda de la tabla estática"
    ):
        sandbox_page.navigate_sandbox()
        valor_inicial = sandbox_page.get_valor_celda_estatica(2, 3)
    with allure.step(
        "Cuando hago una recarga de la página y tomo el valor de la misma celda"
    ):
        sandbox_page.reload_page()
        valor_post_recarga = sandbox_page.get_valor_celda_estatica(2, 3)
    with allure.step(
        "Puedo verificar que el valor efectivamente no se modificó con la recarga de la página."
    ):
        assert (
            valor_inicial == valor_post_recarga
        ), f"El valor de la celda cambió después de la recarga; aún es '{valor_inicial}'."
