
cp .odoo.conf .odoo1.conf
cat .env | sed  's/###//g' > .odoo.conf
echo '\n' >> .odoo.conf
if [ ! -f ".odoo1.conf" ]; then
  touch .odoo1.conf
fi

cat .odoo1.conf | sed -e '1,/#END/ d' | sed '/^$/d' >> .odoo.conf 
cat .odoo.conf