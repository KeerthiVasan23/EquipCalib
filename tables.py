from flask_table import Table, Col, LinkCol


class Resultsupdate(Table):			#HISTORY	
    id = Col('Id', show=False)
    itemcode = Col('Instrument ID')
    masterref=Col('Master Refernce')
    chkdate=Col('Check Date')
    nextcalib=Col('Next Date')
    sd1=Col('Set 1')
    sd2=Col('Set 2')
    sd3=Col('Set 3')
    sd4=Col('Set 4')
    sd5=Col('Set 5')
    od1=Col('Obs 1')
    od2=Col('Obs 2')
    od3=Col('Obs 3')
    od4=Col('Obs 4')
    od5=Col('Obs 5')

class mResultsupdate(Table):			#HISTORY	
    id = Col('Id', show=False)
    itemcode = Col('Instrument ID')
    masterref=Col('Master Refernce')
    chkdate=Col('Check Date')
    nextcalib=Col('Next Date')
    gmajd1=Col('Go maj. dia1.')
    ngmajd1=Col('No go maj. dia1.')
    geffd1=Col('Go eff. dia1.')
    ngeffd1=Col('No go eff. dia1.')
    gpitd1=Col('Go pitch. dia1.')
    ngpitd1=Col('No go pitch. dia1.')
    gmajd2=Col('Go maj. dia2.')
    ngmajd2=Col('No go maj. dia2.')
    geffd2=Col('Go eff. dia2.')
    ngeffd2=Col('No go eff. dia2.')
    gpitd2=Col('Go pitch. dia2.')
    ngpitd2=Col('No go pitch. dia2.')

class Resultsview(Table):                        #MASTER
    id = Col('Id', show=False)
    itemcode = Col('Instrument ID')
    rangee=Col('Range')
    freq=Col('Day')
    #lastedit=Col('Last Date')
    '''nextcalib=Col('Next Date')'''
    locid=Col('Location ID')
    
    
