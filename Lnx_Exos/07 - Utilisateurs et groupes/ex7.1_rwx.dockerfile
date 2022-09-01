chown -R nom1:admin /entreprise/admin/direction/

chmod -R u+w,g-x,o=rx /entreprise/common/

chmod -R u=wx,g-x,o-x /entreprise/documents/nom1
chmod -R u=wx,g-x,o-x /entreprise/documents/nom2
chmod -R u=wx,g-x,o-x /entreprise/documents/nom3

chmod -R 775 /entreprise