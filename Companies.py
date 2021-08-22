class Company:
    """The Purpose of this class is to format the contents of files
    for the purpose of placing them into an output file."""
    cid = ""
    nme = ""
    cntct = ""
    adr = ""
    cit = ""
    stt = ""
    zipc = ""
    phne = ""
    altphne = ""
    keycd = ""
    cmpcd = ""
    rgn = ""
    lmt = ""
    ctype = ""

    def __init__(self, identity, name, contact, address, city, state, zipcode, phone,
                 altPhone, keycode, compCode, region, limit, customerType):
        """ This part identifies the parts where each row will be displayed. """
        self.cid = identity
        self.nme = name
        self.cntct = contact
        self.adr = address
        self.cit = city
        self.stt = state
        self.zipc = zipcode
        self.phne = phone
        self.altphne = altPhone
        self.keycd = keycode
        self.cmpcd = compCode
        self.rgn = region
        self.lmt = limit
        self.ctype = customerType

    def print_cid(self):
        """ This method returns the company ID. The value is left padded
        10 spaces with a capital X. """
        a = ('{:X>10}'.format(self.cid[0:10]))
        return a

    def print_nme(self):
        """ This method returns the name of the company itself, but only if it's
         20 characters long. Left padded with 20 spaces. """
        b = ('{:>20}'.format(self.nme[0:20]))
        return b

    def print_lastName(self):
        """ This method returns the last name of the company contact. Left
         padded 15 spaces. """
        last = self.cntct.split()[1]
        c = ('{:>15}'.format(last[0:15]))
        return c

    def print_firstName(self):
        """ This method returns the first name of the company contact. Left
         padded 20 spaces"""
        first = self.cntct.split()[0]
        d = ('{:>20}'.format(first[0:20]))
        return d

    def print_adr(self):
        """ This method returns the address of the company, only up to 30 characters.
        Left padded 30 spaces. """
        e = ('{:>30}'.format(self.adr[0:30]))
        return e

    def print_cit(self):
        """ This method returns the city for which the company is located,
        it returns only up to 20 characters. Left padded 20 spaces. """
        f = ('{:>20}'.format(self.cit[0:20]))
        return f

    def print_stt(self):
        """ This method uses if states to replace all the states with
        two letter abbreviations. """
        if self.stt == 'Alabama':
            self.stt = 'AL'
        if self.stt == 'Alaska':
            self.stt = 'AK'
        if self.stt == 'Arizona':
            self.stt = 'AZ'
        if self.stt == 'Arkansas':
            self.stt = 'AR'
        if self.stt == 'California':
            self.stt = 'CA'
        if self.stt == 'Colorado':
            self.stt = 'CO'
        if self.stt == 'Connecticut':
            self.stt = 'CT'
        if self.stt == 'Delaware':
            self.stt = 'DE'
        if self.stt == 'District of Columbia':
            self.stt = 'DC'
        if self.stt == 'Florida':
            self.stt = 'FL'
        if self.stt == 'Georgia':
            self.stt = 'GA'
        if self.stt == 'Hawaii':
            self.stt = 'HI'
        if self.stt == 'Idaho':
            self.stt = 'ID'
        if self.stt == 'Illinois':
            self.stt = 'IL'
        if self.stt == 'Indiana':
            self.stt = 'IN'
        if self.stt == 'Iowa':
            self.stt = 'IA'
        if self.stt == 'Kansas':
            self.stt = 'KS'
        if self.stt == 'Kentucky':
            self.stt = 'KY'
        if self.stt == 'Louisiana':
            self.stt = 'LA'
        if self.stt == 'Maine':
            self.stt = 'ME'
        if self.stt == 'Maryland':
            self.stt = 'MD'
        if self.stt == 'Massachusetts':
            self.stt = 'MA'
        if self.stt == 'Michigan':
            self.stt = 'MI'
        if self.stt == 'Minnesota':
            self.stt = 'MN'
        if self.stt == 'Mississippi':
            self.stt = 'MS'
        if self.stt == 'Missouri':
            self.stt = 'MO'
        if self.stt == 'Montana':
            self.stt = 'MT'
        if self.stt == 'Nebraska':
            self.stt = 'NE'
        if self.stt == 'Nevada':
            self.stt = 'NV'
        if self.stt == 'New Hampshire':
            self.stt = 'NH'
        if self.stt == 'New Jersey':
            self.stt = 'NJ'
        if self.stt == 'New Mexico':
            self.stt = 'NM'
        if self.stt == 'New York':
            self.stt = 'NY'
        if self.stt == 'North Carolina':
            self.stt = 'NC'
        if self.stt == 'North Dakota':
            self.stt = 'ND'
        if self.stt == 'Ohio':
            self.stt = 'OH'
        if self.stt == 'Oklahoma':
            self.stt = 'OK'
        if self.stt == 'Oregon':
            self.stt = 'OR'
        if self.stt == 'Pennsylvania':
            self.stt = 'PA'
        if self.stt == 'Rhode Island':
            self.stt = 'RI'
        if self.stt == 'South Carolina':
            self.stt = 'SC'
        if self.stt == 'South Dakota':
            self.stt = 'SD'
        if self.stt == 'Tennessee':
            self.stt = 'TN'
        if self.stt == 'Texas':
            self.stt = 'TX'
        if self.stt == 'Utah':
            self.stt = 'UT'
        if self.stt == 'Vermont':
            self.stt = 'VT'
        if self.stt == 'Virginia':
            self.stt = 'VA'
        if self.stt == 'Washington':
            self.stt = 'WA'
        if self.stt == 'West Virginia':
            self.stt = 'WV'
        if self.stt == 'Wisconsin':
            self.stt = 'WI'
        if self.stt == 'Wyoming':
            self.stt = 'WY'
        if self.stt == 'Guam':
            self.stt = 'GU'
        if self.stt == 'American Somoa':
            self.stt = 'AS'
        if self.stt == 'Northern Marian Islands':
            self.stt = 'MP'
        if self.stt == 'Puerto Rico':
            self.stt = 'PR'
        if self.stt == 'Virgin Islands':
            self.stt = 'VI'

        return self.stt[0:2]

    def print_zipc(self):
        """ This method returns the Zip Code for the company,
        only printing the first 5 characters. Left padded 5 spaces. """
        if self.zipc[6:]:
            print('#####')
        h = ('{:>5}'.format(self.zipc[0:5]))
        return h

    def print_phne(self):
        """ This method returns the primary phone number of the company.
         It returns only the first 10 characters and also replaces all
         spaces and commas with no space. Left padded 10 spaces. """
        number = self.phne.replace('-', '').replace(' ', '')
        i = ('{:>10}'.format(number[0:10]))
        return i

    def print_altphne(self):
        """ This method returns the alternative phone number for the compnay.
        It returns only the first 10 characters and also replaces all
         spaces and commas with no space. Left padded 10 spaces. """
        altnumber = self.altphne.replace('-', '').replace(' ', '')
        j = ('{:>10}'.format(altnumber[0:10]))
        return j

    def print_keycd1(self):
        """ This method returns the Alpha key value, or the
         first 10 characters of the key code. It will also
        right pad with 0s. """
        k = ('{:0<3}'.format(self.keycd[0:10]))
        return k

    def print_keycd2(self):
        """ This method returns the Beta key value, or the last 26
        characters of the key code. It will also left pad with small case x. """
        l = ('{:x>3}'.format(self.keycd[11:36]))
        return l

    def print_cmpcd(self):
        """ This method returns the company code,
         only the first through seventh character. Left padded 7 spaces. """
        m = ('{:>7}'.format(self.cmpcd[0:7]))
        return m

    def print_rgn(self):
        """ This method returns the region for which the company is located.
         5 characters. It will also right pad with spaces. """
        n = ('{:<5}'.format(self.rgn[0:5]))
        return n

    def print_lmt(self):
        """ This method returns the customer limit as K values. 4 characters.
         Left padded 4 spaces."""
        o = ('{:>4}'.format(self.lmt[0:4]))
        return o

    def print_ctype(self):
        """ This method is the customer type, it only returns a single character.
         Left padded a single space."""
        p = ('{:>1}'.format(self.ctype[0]))
        return p
