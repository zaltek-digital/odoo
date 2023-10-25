
cp .odoo.conf .odoo1.conf
cat .env | sed  's/###//g' > .odoo.conf
echo '\n' >> .odoo.conf
if [ ! -f ".odoo1.conf" ]; then
  touch .odoo1.conf
fi
cat .odoo1.conf | grep admin_passwd | head -1 >> .odoo.conf
cat .odoo.conf