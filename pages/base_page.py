class BasePage:
    """
    te trzy ciapki to jest kometarz do dokumetacji, pojawi sie w wielu miejsca, sprawdzic dokladnie po co to
    Base Page Object for each page
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        # site autotest
        return   #czym sie rozni return od pass?

