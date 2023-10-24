
cp .odoo.conf .odoo1.conf
cat .env | sed  's/###//g' > .odoo.conf
echo '\n' >> .odoo.conf
cat .odoo1.conf | sed -e '1,/#END/ d' | sed '/^$/d' >> .odoo.conf 
cat .odoo.conf