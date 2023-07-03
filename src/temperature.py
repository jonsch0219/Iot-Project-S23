import machine

def getTemperature(filter_size):
    
    adc = machine.ADC(27)
    sf = 4095/65535 # Scale factor
    volt_per_adc = (3.3 / 4095)

    temp = 0
    i = 0

    while i < filter_size:
        millivolts = adc.read_u16()

        adc_12b = millivolts * sf

        volt = adc_12b * volt_per_adc

        # MCP9700 characteristics
        dx = abs(50 - 0)
        dy = abs(0 - 0.5)

        shift = volt - 0.5

        temp += (shift/(dy/dx))/filter_size
        
        i += 1

    return temp
