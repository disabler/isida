#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
#                                                                             #
#    Plugin for iSida Jabber Bot                                              #
#    Copyright (C) 2012 diSabler <dsy@dsy.name>                               #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
# --------------------------------------------------------------------------- #

def whowas(type, jid, nick, text):
	period = int(time.time()-86400)
	text = '%%%s%%' % text if text else '%'
	mdb = sqlite3.connect(agestatbase, timeout=base_timeout)
	cu = mdb.cursor()
	was_here = cu.execute('select nick from age where room=?\
												  and time>?\
												  and status=1\
												  and (nick like ? or jid like ?)\
												  group by jid,nick order by nick;',(jid,period,text,text)).fetchall()
	mdb.close()
	if was_here: msg = L('For a last day i see: %s') % ', '.join([t[0] for t in was_here])
	else:msg = L('All who i see for a last day now is here.')
	send_msg(type, jid, nick, msg)

global execute

execute = [(3, 'whowas', whowas, 2, L('Show list of users for last day'))]
