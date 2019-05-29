# pod utils - lower level functions related to omnipod

def getActionDict():
    # this is the list of messages that should be sequential for a successful "action"
    # actionDict {
    #     'actionName' : (idxToNameForSearch list ('sendName', 'recvName','sendName', 'recvName'),
    #     'actionName' : (idxToNameForSearch list ('sendName', 'recvName')
    #             }
    #  Note that this doesn't include any init only actions which are
    #   handled by the pod_progress value
    # These will be searched for in this order and those indices removed from
    #   frameBalance before the next search (see checkAction)

    actionDict = {
      'TB'              : (2, ('1f02', '1d', '1a16', '1d')),
      'Bolus'           : (2, ('0e',   '1d', '1a17', '1d')),
      'Basal'           : (2, ('1f07', '1d', '1a13', '1d')),
      'StatusCheck'     : (0, ('0e'  , '1d')),
      'AcknwlAlerts'    : (0, ('0x11', '1d')),
      'CnfgAlerts'      : (0, ('0x19', '1d')),
      'DeactivatePod'   : (0, ('0x1c', '1d')),
      'DiagnosePod'     : (0, ('0x1e', '1d')),
      'CancelDelivery'  : (0, ('1f'  , '1d')),
      'CancelBasal'     : (0, ('1f01', '1d')),
      'CancelTB'        : (0, ('1f02', '1d')),
      'CancelBolus'     : (0, ('1f04', '1d')),
      'CancelAll'       : (0, ('1f07', '1d'))
       }

    return actionDict
