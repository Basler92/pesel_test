from selenium import webdriver
import unittest

class PeselValidationTest(unittest.TestCase):
    
    def setUp(self):
        # Uruchomienie przeglądarki
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Podaj ścieżkę do chromedriver

        # Otwarcie strony do testowania
        self.driver.get("https://example.com")  # Podaj rzeczywisty adres strony

    def test_valid_pesel(self):
        # Wprowadzenie prawidłowego numeru PESEL
        pesel_input = self.driver.find_element_by_id("pesel_input")  # Znajdź element za pomocą id
        pesel_input.send_keys("88010212345")  # Przykładowy poprawny numer PESEL

        # Kliknij przycisk sprawdzający
        check_button = self.driver.find_element_by_id("check_button")  # Znajdź przycisk za pomocą id
        check_button.click()

        # Sprawdź, czy komunikat o poprawności numeru PESEL jest widoczny
        result_message = self.driver.find_element_by_id("result_message")  # Znajdź element informujący o wyniku
        self.assertTrue(result_message.is_displayed())
        self.assertEqual(result_message.text, "Numer PESEL jest poprawny.")

    def test_invalid_pesel(self):
        # Wprowadzenie nieprawidłowego numeru PESEL
        pesel_input = self.driver.find_element_by_id("pesel_input")  # Znajdź element za pomocą id
        pesel_input.send_keys("12345678901")  # Przykładowy niepoprawny numer PESEL

        # Kliknij przycisk sprawdzający
        check_button = self.driver.find_element_by_id("check_button")  # Znajdź przycisk za pomocą id
        check_button.click()

        # Sprawdź, czy komunikat o błędzie numeru PESEL jest widoczny
        result_message = self.driver.find_element_by_id("result_message")  # Znajdź element informujący o wyniku
        self.assertTrue(result_message.is_displayed())
        self.assertEqual(result_message.text, "Numer PESEL jest niepoprawny.")

    def tearDown(self):
        # Zamknięcie przeglądarki po zakończeniu testu
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
