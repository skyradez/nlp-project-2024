import NLPModelDataSource from "../NLPModelDataSource.ts";
import {NLPModel} from "../../../domain/model/NLPModel.ts";
import axios from "axios";
import {NLPModelEntity} from "./entity/NLPModelEntity.ts";

const BASE_URL = "http://62.72.23.195:9002/model";

export default class NLPModelDataSourceImpl implements NLPModelDataSource {
    private axiosInstance = axios.create({
        baseURL: BASE_URL,
        transformResponse: [function (response) {
            let resp

            try {
                resp = JSON.parse(response)
            } catch (error) {
                throw Error(`[requestClient] Error parsing response JSON data - ${JSON.stringify(error)}`)
            }

            if (resp.status === 'OK') {
                if (resp.data) {
                    return (resp.data as NLPModelEntity)
                }
                return resp.data
            } else {
                throw Error(`[requestClient] Request failed with reason -  ${response}`)
            }
        }]
    })

    async translate(sentence: string): Promise<NLPModel> {
        try {
            const response = await this.axiosInstance({
                method: "post",
                url: "predict/",
                data: {
                    sentence: sentence
                }
            })
            return response.data
        } catch (error) {
            console.log(error)
            throw error
        }
    }

}