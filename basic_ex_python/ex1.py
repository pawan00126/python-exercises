# Ex-1 
import random 
import datetime


def generate_otp(length = 6):
    start = 10**6
    end = 10**7 - 1
    print(start)
    print(end)
    return random.randint(start, end)

# print(generate_otp())


# # Example output: "Your Delhivery shipment ABC123 is In Transit"

def generate_message(courier_name, tracking_id, status = 'In Transit'):
    msg = f'Your shipment with {courier_name} ( AWB : {tracking_id}) is in status : {status}'
    return msg

# print(generate_message('delhivery', 'AWB1234'))



def calculate_shipping_charge(weight_kg, rate_kg = 50, discount_percent = 0):
    charges = weight_kg*rate_kg
    print('charges:',charges)
    final_charges = charges - (charges*discount_percent)/100
    
    return final_charges



# print(calculate_shipping_charge(2.5))               # uses defaults
# print(calculate_shipping_charge(2.5, discount_percent=10))
# print(calculate_shipping_charge(2.5, 60, 5))

# ----------------------------------------------------------------------------



def log_courier_events(*events):
    for event in events:
        print(event)

# log_courier_events('Hello', 'Hii', 'In Transit', 'Delivered')


def build_courier_payload(courier_name, **extra):
    payload = {
        'courier_name' : courier_name
    }

    payload.update(extra)
    return payload


print(build_courier_payload("Delhivery", awb="ABC123", weight=1.2))
print(build_courier_payload("Ekart", order_id="ORD456", cod=True))