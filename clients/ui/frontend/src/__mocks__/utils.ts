import {
  ModelRegistryMetadataType,
  ModelRegistryBody,
  ModelRegistryStringCustomProperties,
} from '~/app/types';

export const createModelRegistryLabelsObject = (
  labels: string[],
): ModelRegistryStringCustomProperties =>
  labels.reduce((acc, label) => {
    acc[label] = {
      metadataType: ModelRegistryMetadataType.STRING,
      // eslint-disable-next-line camelcase
      string_value: '',
    };
    return acc;
  }, {} as ModelRegistryStringCustomProperties);

export const mockBFFResponse = <T>(data: T): ModelRegistryBody<T> => ({
  data,
});
