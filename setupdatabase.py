from basic import db, CUSTOMER

db.create_all()

fani  = CUSTOMER('Fani')
stelios = CUSTOMER('Stelios')

print(fani.customer_id)
print(stelios.customer_id)

db.session.add_all([fani,stelios])

db.session.commit()

print(fani.customer_id)
print(stelios.customer_id)