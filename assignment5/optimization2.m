function sse = optimization2(x)
increment= 0.5;
last_see=1;
last_see_dif=1;
see=0.5;
acceptable_error=0.005;
%Loop to make it automaticly
while (see > acceptable_error)
if ( sqrt((see-last_see)^2) > last_see_dif)
    increment=increment/2;
end
last_see_dif=sqrt((see-last_see)^2);
if(see > last_see)
    x= x-increment; 
else
    x=x+increment
end
last_see=see;
%your comment here
fid= fopen('coefficient.inp','w');
if x < 0.01
    x= 0.01;
end
fprintf(fid,'%f',x);
fclose(fid);
%your comment here



% The following for loop removes files of the old abaqus job. 
% Instead of these lines you can copy the abaqus
% environment file (abaqus_v6.env) to your active path and add
% "ask_delete = OFF" to the file, so abaqus will not ask for
% replacing the existing files at each iteration of the optimization.
delList = dir('tissue.*');
for ii = 1: size(delList)
    filename = delList(ii).name;
    ext = filename(end-3:end);
    if(strcmp(ext, '.prt') || strcmp(ext, '.odb') || strcmp(ext, '.msg') || strcmp(ext, '.com') || strcmp(ext, '.stt') || strcmp(ext, '.sta') ...
                           || strcmp(ext, '.tmp') || strcmp(ext, '.sim') || strcmp(ext, '.mdl') || strcmp(ext, '.dat'))
        delete(delList(ii).name);
    end
end

% submit abaqus job
system('abaqus j=tissue interactive');

% Open the file
fid = fopen('tissue.dat','rt');

% find out how long the file is
fseek(fid,0,1);
f_len = ftell(fid);
fseek(fid,0,-1);

%% Retrieve the data from the file
count = 1;
disp_numeric = zeros(1000, 1);
force_numeric = disp_numeric;
while ftell(fid) < f_len
    temp = fgetl(fid); location = strfind(temp,'TOTAL TIME COMPLETED'); % Text preceeding the timestep value
    if ~isempty(location)
        for i = 1:15,
            temp = fgetl(fid);
        end % Skip 14 lines of the file (between timestep line and first line of nodal values
        [~, remain] = strtok(temp);
        [displ,force] = strtok(remain);
        disp_numeric(count) = str2double(displ);  % The 'U2' of the first node (all the nodes have the same displacment)
        force_numeric(count) = str2double(force);  % The 'RF2' of the first node (all the nodes have the same displacment)
        count = count + 1;
    end
end
fclose(fid);
disp_numeric = disp_numeric(1:count-1);
force_numeric = force_numeric(1:count-1);
data = [disp_numeric,force_numeric]; % First column of data is the displacement U2, second column is the reaction force 'RF2' of the reference node


%% Calculate SSE

data_num=data;
%your comment here
data_exp=load('exp_data.txt');
%your comment here
disp_experimental=data_exp(:,1);
force_experimental=data_exp(:,2);
%your comment here
disp_numeric=data_num(:,1);
force_numeric=data_num(:,2);
%your comment here
disp_exp_revised = disp_numeric;
force_exp_revised = interp1(disp_experimental,force_experimental,disp_exp_revised);
%your comment here
ErrorVector=(force_exp_revised - force_numeric)/length(force_numeric);
sse=sum(ErrorVector .^2);

display (['x = ' num2str(x) ', sse = ' num2str(sse)]);
end

