import time
from tkinter.messagebox import askyesno
import PySimpleGUI as sg


def askYesNoGUI(question, window):
    window['-QUESTION-'].update(question)
    window['-IN-'].update("")
    answers = ['yes', 'no']
    answer = None
    ran = False
    while answer not in answers:
        event, values = window.read()  #HAS TO BE IN FOR LOOP OR WILL CRASH
        if event is None or event == 'Exit':
            window['-OUT-'].update("~~EXITING~~")
            time.sleep(1)
            exit()
        elif event == "-IN-" + "_Enter":
            answer = values['-IN-'].lower()
            
            if not ran and answer not in answers:
                window['-OUT-'].update("Please enter either 'Yes' or 'No'")
                ran = True
    window['-OUT-'].update("Please read the question carefully and press 'Enter' to confirm. ")
    return answer

def askQuestionGUI(answers,question, window):
    window['-QUESTION-'].update(question)
    window['-IN-'].update("")
    answer = None
    ran = False
    while answer not in answers:
        event, values = window.read()  #HAS TO BE IN FOR LOOP OR WILL CRASH
        if event is None or event == 'Exit':
            window['-OUT-'].update("~~EXITING~~")
            time.sleep(1)
            exit()
        elif event == "-IN-" + "_Enter":
            answer = values['-IN-'].lower()
            
            if not ran and answer not in answers:
                window['-OUT-'].update("Please enter one of the accepted answers (in parenthesis)")
                ran = True
    window['-OUT-'].update("Please read the question carefully and press 'Enter' to confirm. ")
    return answer

def buIssue(window):
    question = 'Has the Business Unit encountered an Issue? (Yes/No): '
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        customerPrio(window)
    else:
        window['-OUT-'].update("[Solution]: Based on your answer, there's no solution strategy needed!")
        #print("[Solution]: Based on your answer, there's no solution strategy needed!")

def customerPrio(window):
    question = 'Would you like to run a customer prioritization? (Yes/No): '
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        print("[Customer Prioritization]: Your customer prioritization value is: 4.8667")
        window['-OUT-'].update("[Customer Prioritization]: Your customer prioritization value is: 4.8667")
        window.refresh()
        
        #time.sleep(.5)
    safetyConcern(window)


def safetyConcern(window):
    question = 'Is the issue you are facing a major safety concern? (Yes/No): '
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        window['-OUT-'].update("[Solution]: Since you are experiencing a major safety concern, it is recommended that you perform an Impact and risk analysis before performing an UMPIRE.")
        #print('[Solution]: Since you are experiencing a major safety concern, it is recommended that you perform an Impact and risk analysis before performing an UMPIRE.')
    else:
        isSupported(window)

def isSupported(window):
    question = 'Is the unit still under support? (Yes/No): '
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        securityVuln(window)
    else:
        topCustomer(window)

def topCustomer(window):
    question = 'Is the issue affecting a top customer? And/Or is a special situation? (Yes/No): '
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        securityVuln(window)
    else:
        window['-OUT-'].update("[Solution]: Based on your answers, there's no major mitigation strategy needed.")
        #print("[Solution]: Based on your answers, there's no major mitigation strategy needed.") #Introduce marketing and sales
        
def securityVuln(window):
    question = 'Is there a major security vulnerability? (Yes/No): '
    answers = ['yes','no']
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        securityPatch(window)
    else:
        fieldReplaceOrSoftFix(window)

def securityPatch(window):
    question = 'Can the security vulnerability be fixed with a software patch? (Yes/No): '
    soln = ''
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        soln = "[Solution]: Based on your answers, please issue a PSIRT notification and patch with an update. "
    else:
        soln = "[Solution]: Based on your answers, please determin the likelyhood of this security vulnerability. If there's a high likelyhood of a security risk occurring, please release an UMPIRE."
    window['-OUT-'].update(soln)

def fieldReplaceOrSoftFix(window):
    question = 'Can your issue be fixed with a field replacement or software fix? (Yes/No):'
    answer = askYesNoGUI(question, window)
    if answer =='yes': #Sev 1 or 2
        extVsInternal(window)
    else:
        IBComparison(window)

def IBComparison(window):
    quesiton='Please compare the Impacted Install Base with the Overall Install Base \nIs there greater than 1000 units impacted or is more than 5 percent of the install base impacted? (Yes/No): '
    answer = askYesNoGUI(quesiton, window)
    if answer == 'yes':
        afrVsPAfr(window)
    else:
        GPI(window)
def GPI(window):
    question = "Is the GPI reliability ratio less than .7? (Yes/No): "
    answer = askYesNoGUI(question, window)
    if answer == 'yes':
        fixOnFail(window)
    else:
        extVsInternal(window)

def afrVsPAfr(window):
    question = 'Compare the affected Annual Failure Rate with the Predicted Annual Failure Rate. \nIs the affected AFR (AFR/pAFR): \n    (1) >=2x the pAFR \n    (2) 1.5x <= AFR/pAFR < 2 \n    (3) <1.5x the pAFR \n(1/2/3): '
    answers = ['1','2','3']
    answer = askQuestionGUI(answers, question, window)
    if answer == '1':
        cost(window)
    elif answer == '3':
        fixOnFail(window)
    else:
        lifeCycle(window)

def fixOnFail(window):
    window['-OUT-'].update("[Solution]: Please deploy a Fix on Fail solution. ")
    #print("[Solution]: Please deploy a Fix on Fail solution. ")

def lifeCycle(window):
    question = "What part of its lifecycle is the product in? (Early/Middle/End): "
    answers = ['early','middle','end']
    answer = askQuestionGUI(answers, question, window)
    if answer == 'middle' or answer == 'early':
        cost(window)
    else:
        window['-OUT-'].update("[Solution]: Since the product is not in the reliability part of its lifecycle, the failures rates are expected and no immediate solution strategy is needed. ")
        #print("[Solution]: Since the product is not in the reliability part of its lifecycle, the failures rates are expected and no immediate solution strategy is needed. ")

def cost(window):
    quesiton = 'Which would cost more, performing an UMPIRE or waiting and monitoring the issue? (UMPIRE/Waiting): '
    answers = ['umpire', 'waiting']
    answer = askQuestionGUI(answers, quesiton, window)
    if answer == 'umpire':
        extVsInternal(window)
    else:
        umpire(window)

def umpire(window):
    window['-OUT-'].update("Please issue an UMPIRE. ")
    #print("Please issue an UMPIRE. ")


def extVsInternal(window):
    question = 'Please consult with the BU and determine whether to perform an Internal or External Field Notice (External/Internal): '
    answers = ['external', 'internal']
    answer = askQuestionGUI(answers, question, window)
    soln = ''
    if answer == 'external':
        soln = "[Solution]: Please perform an external field notice and take a reactive approach to fixing this issue. "   
        #print("[Solution]: Please perform an external field notice and take a reactive approach to fixing this issue. ")
    else:
        soln = "[Solution]: Please perform an internal field notice and take a proactive approach to fixing this issue. "
        #print("[Solution]: Please perform an internal field notice and take a proactive approach to fixing this issue. ")
    window['-OUT-'].update(soln)
    

def main():
    sg.theme('LightGreen5')
    layout =[
        [sg.Text('[Question Here]', key='-QUESTION-'), sg.Input(key='-IN-')],
        [sg.Text("Please read the question carefully and press 'Enter' to confirm. ", key = '-OUT-')],
        [sg.Button('OK'), sg.Button('Exit')]]

    window = sg.Window('Field Mitigation Model', layout, finalize = True)
    window.maximize()
    window['-IN-'].bind("<Return>", "_Enter")
    buIssue(window)
    window.refresh()
    time.sleep(10)
    window.close()
if __name__ == "__main__":
    main()