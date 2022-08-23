if __name__ == "__main__":  
#    run_colorsExample()
    import pandas as pd
    import networkx as nx
	import SimpSOM as sps
    
    from sklearn.preprocessing import MinMaxScaler
    pathGE = "C:\\PR_Proj_Thesis\\NEW_SOM_Approach\\BRCA\\GE_withstage_20.csv"
    # Read file 
    df = pd.read_csv(pathGE)
    # Fill na 
    df.fillna(0,inplace = True)
    labels_old = df['TUMOR_STAGE'].values
    df.drop(['TUMOR_STAGE','PATIENT_ID'],axis =1,inplace = True)
    raw_data = df.values
    #Create transpose ; such that each column is one patient
    raw_data = raw_data.T
    
    # applying scaling to make values between some range 0-1/-1-2 ,as need for Kohens SOM
    scaler = MinMaxScaler(copy=True, feature_range=(0, 1))    
    scaler.fit(raw_data)    
    raw_data= scaler.transform(raw_data)
    
    ht = 10
    wd = 10
    no_of_epocs =5
    
    net = sps.somNet(ht,wd, raw_data, PBC=False)

    net.colorEx=False
    
    Learning_rate = 0.05
    net.PCI=True #The weights will be initialised with PCA.
    net.train(Learning_rate,no_of_epocs)   
    col_num = raw_data.shape[0]
    
    node_list = [i for i in range(col_num)]
    new_lbl = [str(j) for j in range(col_num)]
    #new_lbl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416']
#    bmu = net.project(raw_data, labels=new_lbl,name ='SOM',path=p)
    bmu = net.project(raw_data, labels=new_lbl,name ='SOM')
    #print(bmu)
    pos = bmu 
    #pos = [[3.5, 4.330127018922194], [8, 0.0], [9.5, 7.794228634059948], [8.5, 6.062177826491071], [1.5, 7.794228634059948], [3.5, 0.8660254037844388], [6, 0.0], [0, 6.9282032302755105], [8, 1.7320508075688776], [7, 3.4641016151377553], [4.5, 7.794228634059948], [0, 0.0], [9, 0.0], [4, 0.0], [9, 0.0]]
    G=nx.chvatal_graph() 
    nx.draw_networkx_nodes(G,pos,
                       nodelist=node_list,
                       node_color = 'w',
                       edgecolors = [0,0,0],
#                       node_color=[[1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],'b','r','c','y','k','m'],
#                       node_color=[[1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0],'b','r','c','y','k','m'],
                       node_size=1000,alpha=0.8)
    #nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

    new_lbl_dict = dict(enumerate(new_lbl))
    nx.draw_networkx_labels(G,pos,new_lbl_dict,font_size=10)
    
    plt.axis('on')
    plt.show()
    print("EPOCHS  = " , no_of_epocs)
    print("POS = " , pos)
#    plt.savefig('Template.png', bbox_inches='tight', dpi=72)
    print('***************************DONE!!*****************************')