/**
 * 结果集
 * 
 * @property status 状态码
 * @property message 提示信息
 * @property result 携带数据
 */
export interface Result {
    status: number;
    message: string;
    result?: any;
}
