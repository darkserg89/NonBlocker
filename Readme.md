### Программа NonBlocker
Данная программа сделана для предотвращения блокировки экрана во время удаленной работы. 
Каждые 6 минут автоматически нажимаются кнопки изменения громкости, при желание можно использовать другие кнопки.
### Используемые источники
- Использование pyautogui + psgtray: https://pythonrepo.com/repo/PySimpleGUI-psgtray-python-graphical-user-interface-applications
- Использование pyautogui + multiprocessing https://towardsdatascience.com/how-to-keep-windows-from-sleeping-570d2042b338

### Копмпиляция exe файла для windows

Для компиляции используейте следующую команду:
`pyinstaller NonBlocker.spec`