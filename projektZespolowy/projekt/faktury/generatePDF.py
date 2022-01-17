from decimal import Decimal

from fpdf import FPDF
from num2words import num2words

from django.shortcuts import get_object_or_404
from .models import *

def create_table(table_data, title='', data_size=10, title_size=12, align_data='L', align_header='L', cell_width='even',
                 x_start='x_default', emphasize_data=None, emphasize_style=None, emphasize_color=(0, 0, 0), pdf=None):
    if emphasize_data is None:
        emphasize_data = []
    default_style = pdf.font_style
    if emphasize_style == None:
        emphasize_style = default_style

    def get_col_widths():
        col_width = cell_width
        if col_width == 'even':
            col_width = pdf.epw / len(data[0]) - 1
        elif col_width == 'uneven':
            col_widths = []

            for col in range(len(table_data[0])):  # for every row
                longest = 0
                for row in range(len(table_data)):
                    cell_value = str(table_data[row][col])
                    value_length = pdf.get_string_width(cell_value)
                    if value_length > longest:
                        longest = value_length
                col_widths.append(longest + 4)  # add 4 for padding
            col_width = col_widths

        elif isinstance(cell_width, list):
            col_width = cell_width
        else:
            col_width = int(col_width)
        return col_width

    if isinstance(table_data, dict):
        header = [key for key in table_data]
        data = []
        for key in table_data:
            value = table_data[key]
            data.append(value)
        data = [list(a) for a in zip(*data)]

    else:
        header = table_data[0]
        data = table_data[1:]

    line_height = pdf.font_size * 2.5

    col_width = get_col_widths()
    pdf.set_font(size=title_size)

    if x_start == 'C':
        table_width = 0
        if isinstance(col_width, list):
            for width in col_width:
                table_width += width
        else:
            table_width = col_width * len(table_data[0])
        margin_width = pdf.w - table_width

        center_table = margin_width / 2  # only want width of left margin not both
        x_start = center_table
        pdf.set_x(x_start)
    elif isinstance(x_start, int):
        pdf.set_x(x_start)
    elif x_start == 'x_default':
        x_start = pdf.set_x(pdf.l_margin)

    if title != '':
        pdf.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=pdf.font_size)
        pdf.ln(line_height)

    pdf.set_font(size=data_size)

    y1 = pdf.get_y()
    if x_start:
        x_left = x_start
    else:
        x_left = pdf.get_x()
    x_right = pdf.epw + x_left
    if not isinstance(col_width, list):
        if x_start:
            pdf.set_x(x_start)
        for datum in header:
            pdf.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3,
                           max_line_height=pdf.font_size)
            x_right = pdf.get_x()
        pdf.ln(line_height)
        y2 = pdf.get_y()
        pdf.line(x_left, y1, x_right, y1)
        pdf.line(x_left, y2, x_right, y2)

        for row in data:
            if x_start:
                pdf.set_x(x_start)
            for datum in row:
                if datum in emphasize_data:
                    pdf.set_text_color(*emphasize_color)
                    pdf.set_font(style=emphasize_style)
                    pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3,
                                   max_line_height=pdf.font_size)
                    pdf.set_text_color(0, 0, 0)
                    pdf.set_font(style=default_style)
                else:
                    pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3,
                                   max_line_height=pdf.font_size)
            pdf.ln(line_height)

    else:
        if x_start:
            pdf.set_x(x_start)
        for i in range(len(header)):
            datum = header[i]
            pdf.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3,
                           max_line_height=pdf.font_size)
            x_right = pdf.get_x()
        pdf.ln(line_height)  # move cursor back to the left margin
        y2 = pdf.get_y()
        pdf.line(x_left, y1, x_right, y1)
        pdf.line(x_left, y2, x_right, y2)

        for i in range(len(data)):
            if x_start:
                pdf.set_x(x_start)
            row = data[i]
            for i in range(len(row)):
                datum = row[i]
                if not isinstance(datum, str):
                    datum = str(datum)
                adjusted_col_width = col_width[i]
                if datum in emphasize_data:
                    pdf.set_text_color(*emphasize_color)
                    pdf.set_font(style=emphasize_style)
                    pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3,
                                   max_line_height=pdf.font_size)
                    pdf.set_text_color(0, 0, 0)
                    pdf.set_font(style=default_style)
                else:
                    pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3,
                                   max_line_height=pdf.font_size)
            pdf.ln(line_height)  # move cursor back to the left margin
    y3 = pdf.get_y()
    pdf.line(x_left, y3, x_right, y3)


def generateInvoice(invoice_id):
    data = [
        ["Lp.", "Nazwa towaru / usługi", "Ilość", "Cena netto", "VAT", "Wartość netto", "Wartość VAT", "Wartość brutto"]
    ]
    summary = [["Razem", "X", " ", " ", " "]]
    for _ in range(3):
        summary.append(['' for x in range(5)])

    invoice = get_object_or_404(Invoice, pk=invoice_id)
    service_list = Service_Invoice.objects.filter(invoice_id=invoice_id)
    x = 0
    sum_netto = 0
    sum_netto_23 = 0
    sum_netto_8 = 0
    sum_netto_5 = 0
    sum_vat = 0
    sum_vat_23 = 0
    sum_vat_8 = 0
    sum_vat_5 = 0
    sum_brutto = 0
    sum_brutto_23 = 0
    sum_brutto_8 = 0
    sum_brutto_5 = 0

    for service in service_list:
        product = Service.objects.filter(pk=service.service.id)
        ilosc = service.quantity
        x += 1
        data.append((str(x) + ".", product[0].name, str(ilosc), str(product[0].unit_price),
                     str(product[0].tax_rate * 100) + "%", str(product[0].unit_price * ilosc),
                     str(round(product[0].unit_price * ilosc * product[0].tax_rate, 2)),
                     str(round(product[0].unit_price * ilosc + product[0].unit_price * ilosc * product[0].tax_rate, 2))))
        sum_netto += product[0].unit_price * ilosc
        if float(product[0].tax_rate) == 0.23:
            sum_netto_23 += product[0].unit_price * ilosc
        if float(product[0].tax_rate) == 0.8:
            sum_netto_8 += product[0].unit_price * ilosc
        if float(product[0].tax_rate) == 0.5:
            sum_netto_5 += product[0].unit_price * ilosc

        sum_vat += product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.23:
            sum_vat_23 += product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.8:
            sum_vat_8 += product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.5:
            sum_vat_5 += product[0].unit_price * ilosc * product[0].tax_rate

        sum_brutto += product[0].unit_price * ilosc + product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.23:
            sum_brutto_23 += product[0].unit_price * ilosc + product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.8:
            sum_brutto_8 += product[0].unit_price * ilosc + product[0].unit_price * ilosc * product[0].tax_rate
        if float(product[0].tax_rate) == 0.5:
            sum_brutto_5 += product[0].unit_price * ilosc + product[0].unit_price * ilosc * product[0].tax_rate

    summary[0][0] = "Razem"
    summary[0][1] = "X"
    summary[1][0] = "W tym"
    summary[1][1] = "23%"
    summary[2][0] = " "
    summary[2][1] = "8%"
    summary[3][0] = " "
    summary[3][1] = "5%"

    summary[0][2] = str(round(sum_netto, 2))
    summary[1][2] = str(round(sum_netto_23, 2))
    summary[2][2] = str(round(sum_netto_8, 2))
    summary[3][2] = str(round(sum_netto_5, 2))
    summary[0][3] = str(round(sum_vat, 2))
    summary[1][3] = str(round(sum_vat_23, 2))
    summary[2][3] = str(round(sum_vat_8, 2))
    summary[3][3] = str(round(sum_vat_5, 2))
    summary[0][4] = str(round(sum_brutto, 2))
    summary[1][4] = str(round(sum_brutto_23, 2))
    summary[2][4] = str(round(sum_brutto_8, 2))
    summary[3][4] = str(round(sum_brutto_5, 2))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)

    pdf.add_font('DejaVu', '', 'faktury\DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 18)

    pdf.cell(60)
    pdf.cell(90, 20, "Faktura nr:  " + str(invoice.number), 0, 2, align='C')
    pdf.cell(10, 5, " ", 0, 2, 'C')
    pdf.cell(75, 2, " ", 0, 0, 'L')

    pdf.set_font('DejaVu', '', 12)
    pdf.cell(30, 6, 'Miejsce wystawienia: ' + str(invoice.seller.address.city.name), 0, 2, 'L')
    pdf.cell(30, 6, 'Data wystawienia: ' + str(invoice.date_of_issue), 0, 2, 'L')
    pdf.cell(30, 6, 'Data sprzedaży: ' + str(invoice.date_of_payment), 0, 2, 'L')

    pdf.cell(1, 2, " ", 0, 1, 'C')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    pdf.set_font('DejaVu', '', 16)

    pdf.cell(100, 6, 'Sprzedawca', 'B', 0, 'L')
    pdf.cell(30, 6, 'Nabywca', 'B', 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    pdf.set_font('DejaVu', '', 12)
    pdf.cell(100, 6, str(invoice.seller.name), 0, 0, 'L')
    pdf.cell(20, 6, str(invoice.buyer.name), 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    if invoice.seller.address.apartment_number is not None:
        pdf.cell(100, 6, str(
            str(invoice.seller.address.streetname) + " " + str(invoice.seller.address.building_number) + "/" + str(invoice.seller.address.apartment_number)),0, 0, 'L')
    else:
        pdf.cell(100, 6, str(invoice.seller.address.streetname) + " " + str(invoice.seller.address.building_number), 0, 0, 'L')
    if invoice.buyer.address.apartment_number is not None:
        pdf.cell(20, 6, str(invoice.buyer.address.streetname) + " " + str(invoice.buyer.address.building_number) + "/" + str(invoice.buyer.address.apartment_number),0, 1, 'L')
    else:
        pdf.cell(20, 6, str(invoice.buyer.address.streetname) + " " + str(invoice.buyer.address.building_number), 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    pdf.cell(100, 6, str(invoice.seller.address.city.postcode + " " + invoice.seller.address.city.name), 0, 0, 'L')
    pdf.cell(20, 6, str(invoice.buyer.address.city.postcode + " " + invoice.buyer.address.city.name), 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    pdf.cell(20, 6, "NIP: " + str(invoice.seller.nip), 0, 2, 'L')
    pdf.cell(10, 6, " ", 0, 2, 'L')

    pdf.ln(0.5)
    pdf.set_font('DejaVu', '', 11)

    create_table(table_data=data, title='', cell_width='uneven', pdf=pdf)
    pdf.ln()

    create_table(table_data=summary, title='', cell_width=25, x_start=70, pdf=pdf)
    pdf.ln()

    pdf.set_font('DejaVu', '', 11)

    pdf.cell(35, 6, 'Razem:', 0, 0, 'L')
    pdf.cell(50, 6, str(round(sum_brutto, 2)) + " PLN", 0, 0, 'L')
    pdf.cell(20, 6, num2words(round(sum_brutto, 2), lang='pl') + " PLN", 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 1, 'L')
    pdf.cell(35, 6, 'Do zapłaty:', 0, 0, 'L')
    pdf.cell(20, 6, str(round(sum_brutto, 2)) + " PLN", 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 1, 'L')
    pdf.cell(35, 6, 'Termin zapłaty:', 0, 0, 'L')
    pdf.cell(20, 6, str(invoice.date_of_payment), 0, 1, 'L')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 1, 'L')
    pdf.cell(35, 6, 'Data wystawienia:', 0, 0, 'L')
    pdf.cell(20, 6, str(invoice.date_of_issue), 0, 1, 'L')

    pdf.cell(2, 20, " ", 0, 2, 'L')

    pdf.set_font('DejaVu', '', 8)
    pdf.cell(20, 6, ' ', 0, 0, 'C')
    pdf.cell(60, 6, 'Osoba upoważniona do wystawienia', 'T', 0, 'C')
    pdf.cell(30, 6, ' ', 0, 0, 'C')
    pdf.cell(60, 6, 'Osoba upoważnioona do odbioru', 'T', 0, 'C')
    pdf.cell(20, 2, " ", 0, 0, 'L')
    pdf.cell(2, 2, " ", 0, 2, 'L')

    pdf.output('InvoicePDF.pdf')

