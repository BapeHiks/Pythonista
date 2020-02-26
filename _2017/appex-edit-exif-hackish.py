# https://forum.omz-software.com/topic/4101/using-apex-to-modify-a-photo-creation-date-directly/5

import appex
import photos
from objc_util import ObjCInstance

def assets_for_attachments(attachments):
	all_assets = photos.get_assets()
	matching_assets = []
	for a in all_assets:
		path = str(ObjCInstance(a).pathForOriginalFile())
		if path in attachments:
			matching_assets.append(a)
	return matching_assets
	
attachments = appex.get_attachments()
assets = assets_for_attachments(attachments)
# Теперь вы можете использовать модуль photos для управления активами ... (как в предыдущем примере)

