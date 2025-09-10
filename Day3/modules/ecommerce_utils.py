def discount(price,dis_per):
    discount=(price*dis_per*0.01)
    return price-discount
def gst(price,gst_per):
    g=(price*gst_per*0.01)
    return price+g
def invoice(cart,dis_per,gst_per):
    print("------Invoice------")
    t=0
    for i in cart:
        print(i['name'],"₹",i['price'],"x",i['quantity'])
        price=i['price']        
        quantity=i['quantity']
        
      
        amount=price*quantity
    print("Subtotal: ₹",amount)
    print("-------------------------------")
    amount_after_discount=discount(amount,dis_per)
    amount_after_gst=gst(amount_after_discount,gst_per)
    print("After",dis_per,"%","discount: ₹",amount_after_discount)
    print("After",gst_per,"%","GST: ₹",amount_after_gst)
    print("-------------------------------")
    
      