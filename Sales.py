import math

def round_nearest(n, r):
    return (n - math.fmod(n, r)) + 0.05


class SalesTaxes:
    def __init__(self):
        self.inputs = []
        self.output = []
        self.categories = {
            'exclusions': {'chocolate', 'medicine', 'pills', 'book', 'coffee'},
            'import': {'import'}
        }
        self.taxrate = {
            'basic': 0.1,
            'import': 0.05
        }
    
    def dumpOutput(self, output_file = None):
        if not output_file:
            output_file = "output/demo.txt"
        f = open(output_file, "w")
        count = 1
        for otp in self.output:
            f.write("Output {}\n".format(count))
            for line in otp:
                f.write(line)
            count+=1
            f.write('\n')
        return

    def processInput(self):
        for input in self.inputs:
            tax = 0
            output = []
            total = 0
            for items in input:
                product_tax = 0
                imported = False
                quantity = int(items.split(" ")[0])
                name = " ".join((items.split(" at ")[0]).split(' ')[1:])
                price = float(items.split(" ")[-1])
                if 'imported' in name:
                    imported = True
                    product_tax += price * self.taxrate['import']
                
                if not any(exc in name.lower() for exc in self.categories['exclusions']):
                    product_tax += price * self.taxrate['basic']
                total += price
                price += product_tax
                tax += product_tax
                price = float('{:0.2f}'.format(price))
                output.append("{} {}: {:0.2f}\n".format(quantity, name, price))


            tax = round(round_nearest(tax, 0.05),2)
            total += tax
            output.append("Sales Taxes: {:0.2f}\n".format(tax))
            output.append("Total: {:0.2f}\n".format(total))
            self.output.append(output)
        return

    def getInputFile(self,file_name = None):
        input = []
        if not file_name:
            file_name = "inputs/demo.txt"
        f = open(file_name, "r")
        for line in f:
            if 'Input' in line:
                continue
            elif line == '\n':
                self.inputs.append(input)
                input = []
            else:
                input.append(line)
        f.close()
        
        if input not in self.inputs:
            self.inputs.append(input)
        return
    
if __name__ == "__main__":
    ST = SalesTaxes()
    ST.getInputFile()
    ST.processInput()
    ST.dumpOutput()