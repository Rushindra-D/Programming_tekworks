import ecommerce_utils

cart=[{'name':'laptop','price':50000,'quantity':2},
      {'name':'mobile','price':20000,'quantity':3},
      {'name':'tablet','price':15000,'quantity':1}]
dis_per=10
gst_per=18
ecommerce_utils.invoice(cart,dis_per,gst_per)
