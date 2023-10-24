# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.database import Database



class ZaltekController(Database):

    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):
        # context = self._context

        uid = request.env.context.get('uid')
        if( not uid ) :
            return http.request.render('website.page_404')
        
        user = request.env['res.users'].browse(uid)

        if( not user ) :
            return http.request.render('website.page_404')

        if( not user._is_admin() ) :
            return http.request.render('website.page_404')
        
        return super(ZaltekController, self).manager()

    
