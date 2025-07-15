from selene import browser, be, have, by

def test_duckduck_should_find_selene():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene'))

def test_duckduck_nothing_find():
    browser.element('[name="q"]').should(be.blank).type(
        '546лпмтаоаатоео556').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))
    print('не найдено результатов')