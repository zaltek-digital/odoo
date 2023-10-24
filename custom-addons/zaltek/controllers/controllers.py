# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound
from odoo.addons.web.controllers.database import Database

class ZaltekController(Database):

    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):
        uid = request.env.context.get('uid')
        if( not uid ) :
            raise Forbidden()  
            # return http.request.render('website.page_404')
        
        user = request.env['res.users'].browse(uid)

        if( not user ) :
            raise Forbidden()  

        if( not user._is_admin() ) :
            raise Forbidden()
        
        return super(ZaltekController, self).manager()

    
