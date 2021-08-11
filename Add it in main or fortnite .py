@client.event
async def event_party_invite(invite):
    if data[''].lower() == 'true':
        try:
            await invite.accept()
            print(Fore.BLUE + ' [+] ' + Fore.RESET + f'Joined {invite.sender.display_name}')
        except Exception:
            pass
    elif data['joinoninvite'].lower() == 'false':
        if invite.sender.id in info['']:
            await invite.accept()
            print(Fore.BLUE + ' [+] ' + Fore.RESET + 'Joined ' + Fore.LIGHTGREEN_EX + f'{invite.sender.display_name}')
        else:
            print(Fore.RED + ' [+] ' + Fore.RESET + f'Didnt join {invite.sender.display_name}')
