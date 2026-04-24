import numpy as np
import torch
def conv_2d_1x1(x,w):
    #输入 x [bc,8,16,16],
    #输入 w [bc,1,8],
    bc_x,chanel_in,W_x,H_x = x.shape
    bc_w,chanel_out,chanel_in= w.shape
    out = np.zeros((bc_x,chanel_out,W_x,H_x))
    if ( bc_x != bc_w ):
        return
    
    print('sta')
    bc_x_i = 0
    #for bc_x_i in range(0,bc_x):
    for chanel_out_i in range(0,chanel_out,2):
            for H_x_i in range(0,H_x,2):
                for W_x_i in range(0,W_x,2):
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in

                    W_x_i = W_x_i + 1 #特征图W维度并行
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in                       

                H_x_i = H_x_i + 1 #特征图H维度并行
                for W_x_i in range(0,W_x,2):
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in

                    W_x_i = W_x_i + 1 #特征图W维度并行
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in                   
            
            chanel_out_i = chanel_out_i + 1 #输出通道2并行
            for H_x_i in range(0,H_x,2):
                for W_x_i in range(0,W_x,2):
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in

                    W_x_i = W_x_i + 1 #特征图W维度并行
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in                       

                H_x_i = H_x_i + 1 #特征图H维度并行
                for W_x_i in range(0,W_x,2):
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in

                    W_x_i = W_x_i + 1 #特征图W维度并行
                    sum_chanel_in = 0
                    for chanel_in_i in range(0,chanel_in,2):
                        # 输入通道2并行
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i] * x[bc_x_i,chanel_in_i,W_x_i,H_x_i]
                        sum_chanel_in += w[bc_x_i,chanel_out_i,chanel_in_i+1] * x[bc_x_i,chanel_in_i+1,W_x_i,H_x_i]
                    out[bc_x_i,chanel_out_i,W_x_i,H_x_i] = sum_chanel_in  

    return out


#from float2binary import dectbin
if __name__ == '__main__':
    batch_size = 1
    input_ch = 4
    output_ch = 4
    image_x = 6
    image_y = 6
    x = np.random.randn(batch_size,input_ch,image_x,image_y)
    x = torch.tensor(x)
    x = torch.round(x)
    # x = torch.abs(x)
    # x = np.array(
    #      [
    #           [
    #                [
    #                     [1,2,3,4,5,6],
    #                     [5,6,7,8,9,10],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18]
    #                ],
    #                [
    #                     [1,2,3,4,5,6],
    #                     [5,6,7,8,9,10],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18]
    #                ],
    #                [
    #                     [1,2,3,4,5,6],
    #                     [5,6,7,8,9,10],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18]
    #                ],
    #                [
    #                     [1,2,3,4,5,6],
    #                     [5,6,7,8,9,10],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18],
    #                     [9,10,11,12,13,14],
    #                     [13,14,15,16,17,18]
    #                ],
    #           ]
    #      ]
    # )

    w = np.ones((batch_size,output_ch,input_ch))
    w   = w *2.0
    # w = np.random.randn(batch_size,output_ch,input_ch)
    # w = torch.tensor(w)


    print('x.shape:',x.shape)
    #print(x)
    print('w.shape:',w.shape)
    #print(w)
    out = conv_2d_1x1(x,w)
    
    print('out.shape:',out.shape)
    print('out_our_write:',out)

    

    model_conv = torch.nn.Conv2d(in_channels=input_ch,out_channels=output_ch,kernel_size=1,stride=1,padding=0,bias=False)
    torch.nn.init.constant(model_conv.weight,2)
    
    #x = torch.randn(1,8,4,4)
    x = torch.tensor(x,dtype=torch.float)
    #print('x:',x)
    #print('--------------x.dtype:',x.dtype)
    out_nn_conv2d = model_conv(x)
    
    print('out_official_nn_conv2d:',out_nn_conv2d)
    w_temp = w.reshape(-1)
    x_temp = x.reshape(-1).type(torch.float16)
    out_temp = out_nn_conv2d.reshape(-1)


    path_input = './input.txt'
    file_input = open(path_input,'w+').close()
    file_input = open(path_input,'a+')
    for i in range(x_temp.shape[0]):
        file_input.write(f'{x_temp[i]}\n')
    file_input.close()

    path_weight = './weight.txt'
    file_weight = open(path_weight,'w+').close()
    file_weight = open(path_weight,'a+')
    for i in range(w_temp.shape[0]):
        file_weight.write(f'{w_temp[i]}\n')
    file_weight.close()


    path_out = './out.txt'
    file_out = open(path_out,'w+').close()
    file_out = open(path_out,'a+')
    for i in range(out_temp.shape[0]):
        file_out.write(f'{out_temp[i]}\n')

    file_out.close()



