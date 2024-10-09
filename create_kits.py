import sender_stand_request
import data

    # Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = name
    # El resultado de la solicitud se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["name"] == name ["name"]

def negative_assert_symbol(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = name

    # El resultado se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["name"] == 400

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_3)

def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_4)

def test_create_kit_caracter_special_in_name_get_success_response():
    negative_assert_symbol(data.kit_body_5)

def test_create_kit_space_in_name_get_success_response():
    negative_assert_symbol(data.kit_body_6)

def test_create_kit_numbers_in_name_get_success_response():
    negative_assert_symbol(data.kit_body_7)

def test_create_kit_no_name_get_error_response():
    negative_assert_symbol(data.kit_body_8)

def test_create_kit_different_parameter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_9)


