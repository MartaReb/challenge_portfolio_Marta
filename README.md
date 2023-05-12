# Challenge_portfolio_Marta

## Task 1: Konfiguracja oprogramowania
### Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?

Cześć! Mam na imię Marta 🙂 

Jakiś czas temu postanowiłam się przebranżowić i zostać testerką oprogramowania. 
Od tego czasu konsekwentnie staram się zdobywać nową wiedzę w zakresie testowania 
oraz poszerzać tę już zdobytą.

Zdecydowałam się na udział w Dare-IT Challenge, ponieważ chciałabym poznać podstawy pisania testów automatycznych,
z czym mam nadzieje będzie też związana moja zawodowa przyszłość. 

### Subtask 4: Zadanie dla chętnych

Wynik testu: 13/14 

## Task 2: Selektory

**login_field_xpath**

* //*[@id="login"]

* //input[@name="login"]

* //*[@id="login-label"]/following-sibling::div/input


**password_field_xpath**

*  //*[@id="password"]

*  //input[@name="password"]

*  //*[text()="Password"]/following-sibling::div/input


**remaind_password_hyperlink_xpath**

*  //div[@class="MuiCardContent-root"]/a

*  //h5/following-sibling::a

*  //*[last()][name()="a"]


**sign_in_button_xpath**

*  //*[@id="__next"]/form/div/div[2]/button

*  //button[@type="submit"]

*  //button[contains(@class, "MuiButtonBase-root")]


**dropdown_language_list_xpath**

*  //*[@id="__next"]/form/div/div[2]/div/div

*  //div[contains(@class, "MuiSelect-root")]

*  //div[contains(@class, "MuiInputBase-root")]/div

## Task 4: Przypadki testowe

[Przykładowe przypadki testowe dla aplikacji Scouts Panel](https://docs.google.com/spreadsheets/d/1M61LP4jmVPXJPkLhAGm3Ap_cufrFDYdIiIHo-g25NOI/edit#gid=0)

## Task 6:  Zgłaszanie błędów i raport z testów
[Błędy znaleziony przez testy automatyczne](https://docs.google.com/spreadsheets/d/1nC0_WXUhKgu-T4y3OaqL0u1jzyrGmKAO0GEPoPvXQkw/edit#gid=0)

[Raport z przeprowadzonych testów automatycznych](https://docs.google.com/document/d/1WgoSn8IIT5IQyRMi-dL7GQSK4DAr2coVu_QfeKt29HI/edit)
