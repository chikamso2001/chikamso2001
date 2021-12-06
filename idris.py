M = '''Mercedes'''
H = '''Honda'''
T = '''Toyota'''

I_V = '''\nInvalid input!!!'''

ride_types = [ M , H , T ]

#This variable stores the actual price value on each rides
M_P = 3300
H_P = 2500
T_P = 2300


#This variables stores the discount value on each rides.
D_M = 0.5 
D_H = 0.5 
D_T = 0.5


#This variable stores the price value after the discount has been deducted.
rp_M = M_P - (M_P * D_M)
rp_H = H_P - (H_P * D_H)
rp_T = T_P - (T_P * D_T)

print('''\t\t\tBAKE's RIDES''')
print('''\t\t\t____________''')

print('''---------------------'''+ M +' , '+ H +' , '+ T +'''---------------------''')


print('''\n√ What type of ride do you prefer? [''' + M + ',' + H + ' or ' + T + ']')
I = input('''>>>''')

print('''\n\t\t\tNOTE!!!\n\tPlease provide "Yes" or "No" answers to other questions.''')


if I.title() == M :
    print('''\n√ The ride price for ''' + M +  ''' is ''' + '₦' + str(M_P) + ''',but a discount of ''' + str(D_M * M_P) + ''' is given.''' )
    print('''\n√ Do you want the ride?''')
    I = input('''>>>''')
    if I.title() == 'Yes':
        print('''\n√ The ride price for a ''' + M + ''' is ₦''' + str(rp_M) ) 
    elif I.title() == 'No':
        print('''\n√ Do you want another ride?''')
        I = input('''>>>''')
        if I.title() == 'Yes':
            print('''\n√ A ''' + H + ' or ' + T + ' ride?')
            I = input('''>>>''')
            if I.title() == H:
                print('''\n√ The ride price for a ''' + H + ''' is ''' + str(H_P) + ''',but a discount of ₦''' + str(H_P * D_H) + ''' is give.''')
                print('''\n√ Do you want the ride?''')
                I = input('''>>>''')
                if I.title() == 'Yes':
                    print('''\n√ The ride price for a ''' + H + ''' is ''' + '''₦''' + str(rp_H))
                elif I.title() == 'No':
                       print('''\n√ We only have a Toyota ride left! \n√√Do you want a Toyota ride?''')
                       I = input('''>>>''')
                       if I.title() == 'Yes':
                          print('''\n√ The ride price for ''' + T + ''' is ''' + '''₦''' + str(T_P) + ''' but a discount of ''' + '''₦''' + str(D_T * T_P) + ''' is given.''')
                          print('''Do you want the ride?''')
                          I = input('''>>>''')
                          if I.title() == 'Yes':
                              print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(rp_T))
                          elif I.title() == 'No':
                              print('''\n\t\tThanks for using this channel!\n\t\t\tBake's ride✓®''')
                          
                       elif I.title() == 'No':
                        print('''\n\t\tThanks for using this channel!\n\t\t\tBake's ride✓®''')
            elif I.title() == T:
                print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(T_P) + ''' but a discount of ''' + '''₦''' + str(D_T * T_P) + ''' is given.''')
                print('''\n√ Do you want the ride?''')
                I = input('''>>>''')
                if I.title() == 'Yes':
                    print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(rp_T))
                elif I.title() == 'No':
                   print('''\n√ We only have a Honda ride left! \nDo you want a Honda ride?''')
                   I = input('''>>>''')
                   if I.title() == 'Yes':
                       print('''\n√ The ride price for a ''' + H + ''' is ''' + str(H_P) + ''',but a discount of ₦''' + str(H_P * D_H) + ''' is give.''')
                       print('''\n√ Do you want the ride?''')
                       I = input('''>>>''')
                       if I.title() == 'Yes':
                           print('''\n√ The ride price for a ''' + H + ''' is ''' + '''₦''' + str(rp_H))
                       elif I.title() == 'No':
                          print('''\n\t\tThanks for using this channel!\n\t\t\tBake's ride✓®''')
                       
                   elif I.title() == 'No':
                       print('''\n\t\tThanks for using this channel!\n\t\t\tBake's ride✓®''')
            
        elif I.title() == 'No':
                   print('''\n\t\tThanks for using this channel \n\t\t\tBAKE's RIDE ™✓''')
        else:
            print(I_V) 

       
elif I.title() == H:
    print('''\n√ The ride price for a ''' + H + ''' is ''' + str(H_P) + ''',but a discount of ₦''' + str(H_P * D_H) + ''' is give.''')
    print('''\n√ Do you want the ride?''')
    I = input('''>>>''')
    if I.title() == 'Yes':
           print('''\n√ The ride price for a ''' + H + ''' is ''' + '''₦''' + str(rp_H))
    elif I.title() == 'No':
           print('''\n√ Do you want another ride?''')
           I = input('''>>>''')
           if I.title() == 'Yes':
                  print('''\n√ A ''' + M + ' or ' + T + ' ride? ')
                  I = input('''>>>''')
                  if I.title() == M:
                      print('''\n√ The ride price for ''' + M +  ''' is ''' + '₦' + str(M_P) + ''',but a discount of ''' + str(D_M * M_P) + ''' is given.''' )
                      print('''Do you want the ride?''')
                      I = input('''>>>''')
                      if I.title() == 'Yes':
                          print('''\n√ The ride price for a ''' + M + ''' is ₦''' + str(rp_M) ) 
                      elif I.title() == 'No':
                          print('''\n√ We only have a Toyota ride left!\n√ Do you want a Toyota ride?''')
                          I = input('''>>>''')
                          if I.title() == 'Yes':
                              print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(T_P) + ''' but a discount of ''' + '''₦''' + str(D_T * T_P) + ''' is given.''')
                              print('''\n√ Do you want the ride?''')
                              I = input('''>>>''')
                              if I.title() == 'Yes':
                                  print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(rp_T))
                              
                              elif I.title() == 'No':
                                  print('''\n\t\tThanks for using this channel \n\t\t\tBAKE's RIDE ™✓''')
                          elif I.title() == 'No':
                             print('''\n\t\tThanks for using this channel \n\t\t\tBAKE's RIDE ™✓''')  
                             
                  elif I.title() == T:
                     print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(T_P) + ''' but a discount of ''' + '''₦''' + str(D_T * T_P) + ''' is given.''')
                     print('''\n√ Do you want the ride?''')
                     I = input('''>>>''')
                     if I.title() == 'Yes':
                         print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(rp_T))
                     elif I.title() == 'No':
                         print('''\n√ We only have a Mercedes ride left!\n√ Do you want a Mercedes ride?''')
                         I = input('''>>>''')
                         if I.title() == 'Yes':
                             print('''\n√ The ride price for ''' + M +  ''' is ''' + '₦' + str(M_P) + ''',but a discount of ''' + str(D_M * M_P) + ''' is given.''' )
                             print('''Do you want the ride?''')
                             I= input('''>>>''')
                            
                             if I.title() == 'Yes':
                                print('''\n√ The ride price for a ''' + M + ''' is ₦''' + str(rp_M) )
                                  
                             elif I.title() == 'No':
                                 print('''\n\t\tThanks for using this channel \n\t\t\tBAKE's RIDE ™✓''') 

                         elif I.title() == 'No':
                          print('''\n\t\tThanks for using this channel \n\t\t\tBAKE's RIDE ™✓''') 


elif I.title() == T:
      print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(T_P) + ''' but a discount of ''' + '''₦''' + str(D_T * T_P) + ''' is given.''')
      print('''\n√ Do you want this ride?''')
      I = input('''>>>''')
      if I.title() == 'Yes':
          print('''\n√ The ride price for a ''' + T + ''' is ''' + '''₦''' + str(rp_T))
      elif I.title() == 'No':
          print('''\n√ Do you want another ride?''')
          I = input('''>>>''')
          if I.title() == 'Yes':
              print('''\n√ A ''' + M + ''' or ''' + H + ''' ride?''')
              I = input('''>>>''')
              if I.title() == M:
                  print('''\n√ The ride price for ''' + M +  ''' is ''' + '₦' + str(M_P) + ''',but a discount of ''' + str(D_M * M_P) + ''' is given.''' )
                  print('''\n√ Do you want this ride?''')
                  I = input('''>>>''')
                  if I.title() == 'Yes':
                      print('''\n√ The ride price for a ''' + M + ''' is ₦''' + str(rp_M) )
                  elif I.title() == 'No':
                      print('''\n√ We only have a Honda ride left!\n√ Do you want a Honda ride?''')
                      I = input('''>>>''')
                      if I.title() == 'Yes':
                          print('''\n√ The ride price for a ''' + H + ''' is ''' + str(H_P) + ''',but a discount of ₦''' + str(H_P * D_H) + ''' is give.''')
                          print('''\n√ Do you want this ride?''') 
                          I = input('''>>>''')
                          if I.title() == 'Yes':
                              print('''\n√ The ride price for a ''' + H + ''' is ''' + '''₦''' + str(rp_H))
                          elif I.title() == 'No':
                              print('''\n\t\t√ Thanks for using this channel!\n\t\t\t BAKE's RIDE ✓™''')
                      elif I.title() == 'No':
                           print('''\n\t\t√ Thanks for using this channel!\n\t\t\tBAKE's RIDE ✓™''')


              elif I.title() == H:
                  print('''\n√ The ride price for a ''' + H + ''' is ''' + str(H_P) + ''',but a discount of ₦''' + str(H_P * D_H) + ''' is give.''')
                  print('''\n√ Do you want the ride?''')
                  I = input('''>>>''')
                  if I.title() == 'Yes':
                            print('''\n√ The ride price for a ''' + H + ''' is ''' + '''₦''' + str(rp_H))
                  elif I.title() == 'No':
                           print('''\n√ We only have a Mercedes ride left!\n√ Do you want a Mercedes ride?''')
                           I = input('''>>>''')
                           if I.title() == 'Yes':
                                   print('''\n√ The ride price for ''' + M +  ''' is ''' + '₦' + str(M_P) + ''',but a discount of ''' + str(D_M * M_P) + ''' is given.''' )
                                   print('''\n√ Do you want this ride?''')
                                   I = input('''>>>''')
                                   if I.title() == 'Yes':
                                       print('''\n√ The ride price for a ''' + M + ''' is ₦''' + str(rp_M) )
                                   elif I.title() == 'No':
                                       print('''\n\t\t√ Thanks for using this channel!\n\t\t\tBAKE's RIDE ✓™''')
                                   
                           elif I.title() == 'No':
                               print('''\n\t\t√ Thanks for using this channel!\n\t\t\tBAKE's RIDE ✓™''')
                               
                                    
else:
    print(I_V)     
                          
                     
                                                               
                                  